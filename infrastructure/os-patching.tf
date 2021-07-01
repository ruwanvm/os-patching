# Install patches to Master instance
resource "null_resource" "setup-packages" {
    provisioner "local-exec" {
      command = "ansible-playbook -u ${local.ssh_user} -i ${aws_instance.master_ami.public_ip}, --private-key ${var.private_key_file} ../configuration/os_patching_playbook.yml -e repo_location=${var.repo_location} -e repo_date=${var.repo_date} -e instance_id=${aws_instance.master_ami.id} -e region=${var.region} -e public_ip=${aws_instance.master_ami.public_ip}"
    }

    depends_on = [
        aws_instance.master_ami
    ]
}