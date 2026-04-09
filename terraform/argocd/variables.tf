variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "cluster_name" {
  type    = string
  default = "eks-cluster"
}

variable "argocd_namespace" {
  type    = string
  default = "infra-tools"
}
