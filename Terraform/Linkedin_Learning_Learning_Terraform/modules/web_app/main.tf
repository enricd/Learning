# load balancer
resource "aws_elb" "this"{
  name            = "${var.web_app}-web"
  subnets         = var.subnets
  security_groups = var.security_groups

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  tags = {
    "Terraform" : "true"
  }
}

resource "aws_launch_template" "this" {
  name_prefix = "${var.web_app}-web"
  image_id = var.web_image_id
  instance_type = var.web_instance_type
  tags = {
    "Terraform" = "true"
  }
}

resource "aws_autoscaling_group" "this" {
  availability_zones  = ["us-west-1a", "us-west-1b"]
  vpc_zone_identifier = var.subnets
  desired_capacity    = var.web_desired_capacity
  max_size            = var.web_max_size
  min_size            = var.web_min_size

  launch_template {
    id      = aws_launch_template.this.id
    version = "$Latest"
  }

  tag {
    key                 = "Terraform"
    value               = "true"
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_attachment" "this" {
  autoscaling_group_name = aws_autoscaling_group.this.id
  elb                    = aws_elb.this.id  
}
