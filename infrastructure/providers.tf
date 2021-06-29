terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.44.0"
    }
    null = {
      source = "hashicorp/null"
      version = "3.1.0"
    }
  }
}

provider "aws" {
    profile = "default"
    region  = "us-west-2"
}

provider "null" {
  
}