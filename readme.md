# OS Patching

This terraform plan and Ansible playbook will create a new AMI with OS patching instructions

New AMI should be updated on new version of Launch Templates for GEN1 & GEN2 Autoscaling groups

New Version of Launch Tempalte should be created manually

## 2021-Spring OS patching instructions

Instructions are on CLDWRK-9 ticket

## OS patching repo re-use instructions

Update following variables on Terraform Plan
- base_ami_id
- new_ami_name

## Run ansible playbook independantly
    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u {{ user name }} -i '{{ public ip }},' --private-key {{ private key file }} -e {{ repo date }} {{ playbook name }}