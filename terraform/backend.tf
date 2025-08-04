terraform {
  backend "s3" {
    bucket = "news-data-pipeline-rds"
    key    = "terraform.tfstate"
    region = "us-west-1"
  }
}