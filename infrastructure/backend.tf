terraform {
  backend "s3" {
    bucket         = "ust-ops-filestore"
    region         = "us-east-1"
    key            = "terraform/states/terraform-ospatching-gen2-reactor-2021-spring.tfstate"
  }
}