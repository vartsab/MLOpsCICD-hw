## Check ArgoCD
```kubectl get pods -n infra-tools```

## Open ArgoCD UI
```kubectl port-forward svc/argocd-server -n infra-tools 8080:443```

## Get ArgoCD password
```kubectl get secret argocd-initial-admin-secret -n infra-tools -o jsonpath="{.data.password}" | base64 --decode && echo```

## Apply application
```kubectl apply -f application.yaml -n infra-tools```
## Check application
```kubectl get applications -n infra-tools```
```kubectl get pods -n application```
```kubectl get svc -n application```
