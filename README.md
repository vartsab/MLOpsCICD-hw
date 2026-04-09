# MLOps Training Automation Pipeline

End-to-end automated ML training pipeline using AWS Step Functions, Lambda, Terraform, and GitLab CI.

---

## Architecture Overview

This project demonstrates a production-like MLOps workflow:

- Terraform provisions infrastructure
- AWS Lambda handles pipeline steps
- AWS Step Functions orchestrates the workflow
- GitLab CI triggers training automatically on code changes

Pipeline flow:

```
GitLab CI → Step Function → Validate → Log Metrics
```

---

## Project Structure

```
mlops-train-automation/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── lambda/
│       ├── validate.py
│       ├── log_metrics.py
│       ├── validate.zip
│       └── log_metrics.zip
├── .gitlab-ci.yml
├── README.md
```

---

## Lambda Functions

### validate.py

Simulates data validation step:
- Receives input from CI
- Validates payload
- Returns structured response

### log_metrics.py

Simulates metrics logging:
- Receives output from validation step
- Logs pipeline results
- Returns final status

---

##Infrastructure (Terraform)

To deploy infrastructure:

```bash
cd terraform
terraform init
terraform apply
```

This creates:
- IAM roles (Lambda + Step Functions)
- 2 Lambda functions
- Step Function pipeline

---

## Step Function Workflow

The pipeline includes two steps:

1. ValidateData 
2. LogMetrics 

Execution flow:

```
ValidateData → LogMetrics
```

---

## Manual Execution

You can manually trigger the pipeline:

```bash
aws stepfunctions start-execution \
  --region us-east-1 \
  --state-machine-arn <YOUR_STEP_FUNCTION_ARN> \
  --name "manual-test" \
  --input '{"source":"manual","commit":"test"}'
```

---

##  GitLab CI Integration

Pipeline is automatically triggered on push to:

```
lesson-10 branch
```

### CI Job Behavior

- Uses AWS CLI Docker image
- Sends execution request to Step Function
- Passes commit metadata as input

### Example payload:

```json
{
  "source": "gitlab-ci",
  "commit": "abc123"
}
```

---

## Required CI/CD Variables

Set in GitLab:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION = us-east-1
- STEP_FUNCTION_ARN

---

## Result

- Fully automated ML pipeline trigger
- Infrastructure as code (Terraform)
- Reproducible workflow
- CI/CD integration with AWS

---

## Key Takeaways

- CI/CD is not just about code — it’s about orchestration
- Small configuration issues can break entire pipelines
- Cloud automation requires precise environment setup

---

## Author

Denys Vartsab
Data Analyst
