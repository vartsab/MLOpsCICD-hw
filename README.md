# Homework 7 - ArgoCD GitOps

## Terraform: deploy ArgoCD
```cd terraform/argocd```
```terraform init```
```terraform apply -auto-approve```


## Check ArgoCD
```kubectl get pods -n infra-tools```

## Open ArgoCD UI
```kubectl port-forward svc/argocd-server -n infra-tools 8080:80```

## Open:
```http://localhost:8080```

## Get ArgoCD password
```kubectl get secret argocd-initial-admin-secret -n infra-tools -o jsonpath="{.data.password}" | base64 --decode && echo```

## Apply application
```kubectl apply -f application.yaml -n infra-tools```

## Check application deployment
```kubectl get applications -n infra-tools```
```kubectl get pods -n application```
```kubectl get svc -n application```

## Access MLflow
```kubectl port-forward svc/mlflow -n application 5000:5000```

## Open:
```http://localhost:5000```

## GitOps repository
```https://github.com/vartsab/goit-argocd```
