# Lesson 8-9: MLflow + MinIO + PostgreSQL + PushGateway (ArgoCD)

## Environment
- OS: Windows + WSL (Ubuntu)
- AWS Region: us-east-1
- Kubernetes: AWS EKS
- Cluster: eks-cluster

## Deployed services (via ArgoCD)
- MLflow Tracking Server
- PostgreSQL (backend store)
- MinIO (artifact storage)
- Prometheus PushGateway (metrics)

---

## Project structure
mlops-experiments/
```
├── argocd/
│ ├── application.yaml
│ └── applications/
│ ├── postgres.yaml
│ ├── minio.yaml
│ └── pushgateway.yaml
├── experiments/
│ ├── train_and_push.py
│ └── requirements.txt
├── best_model/
│ └── best_model.pkl
└── screenshots/
```
---

##  ArgoCD Applications

```kubectl get applications -n infra-tools```

## Check services
```kubectl get pods -n application```
```kubectl get svc -n application```
```kubectl get pods -n monitoring```
```kubectl get svc -n monitoring```

---

## MLflow
```kubectl port-forward svc/mlflow -n application 5000:5000```
### Open:
```http://localhost:5000```

## MinIO
```kubectl port-forward svc/minio -n application 9000:9000```
```kubectl port-forward svc/minio -n application 9001:9001```
### Open:
```http://localhost:9001```
### Login:
```admin / admin12345```

## PushGateway
```kubectl port-forward svc/pushgateway-prometheus-pushgateway -n monitoring 9091:9091```
### Open:
```http://localhost:9091/metrics```

---

## Run experiment
```cd ~/mlops-experiments```
```source .venv/bin/activate```

```export AWS_ACCESS_KEY_ID=admin```
```export AWS_SECRET_ACCESS_KEY=admin12345```
```export AWS_DEFAULT_REGION=us-east-1```
```export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000```

```python experiments/train_and_push.py```

---

## Expected results
- MLflow UI shows multiple runs
- Parameters and metrics logged
- Artifacts stored in MinIO bucket mlflow-artifacts
- Best model saved locally (```best_model/best_model.pkl```)
- Metrics pushed to PushGateway

## Metrics check
``` curl http://localhost:9091/metrics | grep mlflow_```

---

## Screenshots

- MLflow UI with runs
- MinIO bucket mlflow-artifacts
- PushGateway /metrics page


---

## Result

Fully working MLOps pipeline:
- Experiment tracking (MLflow)
- Artifact storage (MinIO)
- Metadata DB (PostgreSQL)
- Metrics (PushGateway)
- GitOps deployment (ArgoCD)

---

# REQUIREMENTS.TXT

- mlflow
- scikit-learn
- requests
- joblib
- boto3
