variable base_ami_id {
    type = string
    description = "AMI-ID of the base image to create Master machine"    
}

variable "machine_type" {
    type = string
    description = "Master machine AWS Instance type (t2.micro, t2.medium, etc...)"  
}

variable "machine_key" {
    type = string
    description = "Key pair name to SSH Master machine"  
}

variable "security_group" {
    type = string
    description = "Master machine security group ID"  
}

variable "subnet_id" {
    type = string
    description = "Master machine subnet ID"  
}

variable "iam_role" {
    type = string
    description = "IAM Role to attach to Master machine"  
}

variable "machine_name" {
    type = string
    description = "Name of the Master machine"  
}

variable "new_ami_name" {
    type = string
    description = "Name of the Master machine"  
}


variable "script_name" {
    type = string
    description = "Script file to execute"  
}

variable "private_key_file" {
    type = string
    description = "Private key file to SSH"  
}
