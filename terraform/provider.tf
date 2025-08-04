provider "aws" {
  default_tags {
    tags = {
      Environment = "Production"
      Owner       = "Data_Engineering_Team"
      Project     = "RDS-project"
      Managed_by  = "Terraform"
    }
  }
  region = "us-west-1"
}

terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "3.7.2"
    }
  }
}
provider "random" {
  # Configuration options
}