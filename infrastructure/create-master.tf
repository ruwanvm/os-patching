# Create AMI-Master instance to setup Promtail

resource "aws_instance" "ustockdev-gen2-reactor-AMI-master-promtail" {
    ami = var.base_ami_id
    instance_type = var.machine_type
    key_name = var.machine_key
    associate_public_ip_address = true
    vpc_security_group_ids = [ var.security_group ]
    subnet_id = var.subnet_id
    iam_instance_profile = var.iam_role
    
    tags = {
      "Name" = var.machine_name
    }
}

output "Master_Machine-ID" {
  value = aws_instance.ustockdev-gen2-reactor-AMI-master-promtail.id
}

output "Master_Machine-Public_IP" {
  value = aws_instance.ustockdev-gen2-reactor-AMI-master-promtail.public_ip
}