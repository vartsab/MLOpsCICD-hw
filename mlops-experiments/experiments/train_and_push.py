import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import requests
import os
import joblib

mlflow.set_tracking_uri("http://localhost:5000")

PUSHGATEWAY_URL = "http://localhost:9091/metrics/job/mlflow"

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

best_acc = 0
best_model = None

for n_estimators in [10, 50, 100]:
    with mlflow.start_run() as run:
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_metric("accuracy", acc)

        # save model locally + upload to MLflow
        model_path = f"model_{run.info.run_id}.pkl"
        joblib.dump(model, model_path)
        mlflow.log_artifact(model_path)

        # push metric to PushGateway
        metrics_data = f'mlflow_accuracy{{run_id="{run.info.run_id}"}} {acc}'
        requests.post(PUSHGATEWAY_URL, data=metrics_data)

        print(f"Run {run.info.run_id} → accuracy={acc}")

        if acc > best_acc:
            best_acc = acc
            best_model = model

# save best model
os.makedirs("best_model", exist_ok=True)
joblib.dump(best_model, "best_model/best_model.pkl")

print("Best model saved!")
