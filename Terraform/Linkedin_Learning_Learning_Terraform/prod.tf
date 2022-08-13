variable "whitelist" {
  type = list(string)
}
variable "web_instance_type" {
  type = string
}
variable "web_desired_capacity" {
  type = number
}
variable "web_max_size" {
  type = number
}
variable "web_min_size" {
  type = number
}

provider "aws" {
  profile = "default"
  region  = "us-west-1"
}

# storage bucket
resource "aws_s3_bucket" "prod_tf_course" {
  bucket = "tf-course-20220813"       # it has to be unique in the world
  acl    = "private"

  tags = {
    "Terraform" = "true"
  }
}

# vpc
resource "aws_default_vpc" "default" {}

# one subnet per availability zone in each region
resource "aws_default_subnet" "default_az1" {
  availability_zone = "us-west-1a"

  tags = {
    "Terraform" : "true"
  }
}

resource "aws_default_subnet" "default_az2" {
  availability_zone = "us-west-1b"

  tags = {
    "Terraform" : "true"
  }
}

# security group acting as a firewall
resource "aws_security_group" "prod_web" {
  name        = "prod_web"
  description = "Allow standard http and https ports inbound and everything outbound"
  
  ingress {
    from_port   = "80"
    to_port     = "80"
    protocol    = "tcp"
    cidr_blocks = var.whitelist
  }
  ingress {
    from_port   = "443"
    to_port     = "443"
    protocol    = "tcp"
    cidr_blocks = var.whitelist
  }
  egress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "Terraform" : "true"
  }
}

module "web_app" {
  source = "./modules/web_app"

  web_image_id         = var.web_image_id
  web_instance_type    = var.web_instance_type
  web_desired_capacity = var.web_desired_capacity
  web_max_size         = var.web_max_size
  web_min_size         = var.web_min_size
  subnets              = [aws_default_subnet.default_az1.id,aws_default_subnet.default_az2.id]
  security_groups      = [aws_security_group.prod_web.id]
  web_app              = "prod"
}

