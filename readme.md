# OS Patching

This terraform plan and Ansible playbook will create a new AMI with OS patching instructions

New AMI should be updated on new version of Launch Templates for GEN1 & GEN2 Autoscaling groups

New Version of Launch Tempalte should be created manually

## 2021-Spring OS patching instructions

Instructions are on CLDWRK-9 ticket

## OS patching repo re-use instructions

Update following variables on Terraform Plan
- base_ami_id (AMI-ID of the base image to create Master machine)
- new_ami_name (new_ami_name)
- repo_location (Location of the repocitory for os-patching)
- repo_date (Repo date provided with the os-patching instruction)

## Run ansible playbook independantly
    ansible-playbook -u {{ user name }} -i '{{ public ip }},' --private-key {{ private key file path }} -e repo_location={{ repo location }} -e repo_date={{ repo date }} {{ playbook name }}