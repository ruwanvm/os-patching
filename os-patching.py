#!/usr/bin/python

import os
import getpass
from os.path import join

from PyInquirer import style_from_dict, Token, prompt
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(message="Please enter a number",
                                  cursor_position=len(document.text))

def main():
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    os_patching_questions = [
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': f'Hey {getpass.getuser().capitalize()}, Are you starting OS Patching on ustockdev system : ',
            'default': False
        },
        {
            'type': 'input',
            'name': 'year',
            'message': 'OS patching year : ',
            "validate": NumberValidator,
            "filter": lambda val: int(val),
            'when': lambda answers: answers['confirmation'] == True
        },
        {
            'type': 'list',
            'name': 'frequency',
            'message': 'Select Patching frequency : ',
            'choices': ['Spring', 'Fall'],
            'filter': lambda val: val.lower(),
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'list',
            'name': 'app_type',
            'message': 'Select Application type : ',
            'choices': ['tvm', 'reactor', 'ticker'],
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'list',
            'name': 'generation',
            'message': 'Select Generation : ',
            'choices': ['GEN1', 'GEN2'],
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'base_ami_id',
            'message': 'Base AMI ID : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'security_group',
            'default': os.environ.get('DEFAULT_SECURITY_GROUP'),
            'message': 'Security Group : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'subnet_id',
            'default': os.environ.get('DEFAULT_SUBNET'),
            'message': 'Subnet ID : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'iam_role',
            'default': os.environ.get('DEFAULT_IAM_ROLE'),
            'message': 'IAM role to attach : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'region',
            'default': os.environ.get('DEFAULT_REGION'),
            'message': 'AWS Region : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'private_key_file',
            'default': os.environ.get('DEFAULT_PRIVATE_KEY'),
            'message': 'Private Key path : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'repo_date',
            'message': 'REPO DATE : ',
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        },
        {
            'type': 'input',
            'name': 'repo_location',
            'message': 'REPO LOCATION : ',
            'default': os.environ.get('DEFAULT_REPO_LOCATION'),
            'when': lambda answers: answers['confirmation'] == True and answers['year'] >= 2020
        }
    ]

    answers = prompt(os_patching_questions, style=style)

    if answers['confirmation']:
        print("##########################################################################################")
        print(f"{answers['year']}-{answers['frequency']} OS PATCHING STARTED BY {getpass.getuser().capitalize()} !!!")
        print("##########################################################################################")

        answers['machine_type'] = os.environ.get('DEFAULT_MACHINE_TYPE')
        answers['machine_key'] = os.environ.get('DEFAULT_MACHINE_KEY')
        answers['machine_name'] = f"ustockdev-{answers['generation'].lower()}-{answers['app_type']}-AMI-master-patching-{answers['year']}-{answers['frequency']}"
        answers['new_ami_name'] = f"ustockdev-{answers['generation'].lower()}-{answers['app_type']}-AMI-patching-{answers['year']}-{answers['frequency']}"

        del answers['confirmation']
        del answers['year']
        del answers['frequency']
        del answers['app_type']
        del answers['generation']

        with open(join('infrastructure', 'terraform.tfvars'), mode="w") as tfvars_file:
            for key in answers:
                tfvars_file.write(f'{key} = "{answers[key]}"\n')

if __name__ == '__main__':
    main()