terraform {
  backend "s3" {
    bucket         = "denys-terraform-state-2026"
    key            = "hw7/argocd/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "denys-terraform-locks"
    encrypt        = true
  }
}
