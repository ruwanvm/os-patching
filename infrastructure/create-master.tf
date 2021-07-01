# Create AMI-Master instance patch
locals {
  ssh_user         = "ec2-user"
}

resource "aws_instance" "master_ami" {
    ami                         = var.base_ami_id
    instance_type               = var.machine_type
    key_name                    = var.machine_key
    associate_public_ip_address = true
    vpc_security_group_ids      = [ var.security_group ]
    subnet_id                   = var.subnet_id
    iam_instance_profile        = var.iam_role
    
    tags = {
      "Name" = var.machine_name
    }

    provisioner "remote-exec" {
      inline = ["echo 'Wait until SSH is ready'"]

      connection {
        type        = "ssh"
        user        = local.ssh_user
        private_key = file(var.private_key_file)
        host        = aws_instance.master_ami.public_ip
      }
    }    
}

output "Master_Machine-ID" {
  value = aws_instance.master_ami.id
}

output "Master_Machine-Public_IP" {
  value = aws_instance.master_ami.public_ip
}