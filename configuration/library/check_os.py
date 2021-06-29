#!/usr/bin/python

from ansible.module_utils.basic import *
import os

def main():
    value = "Abcdef"
    module = AnsibleModule(argument_spec={})
    response = {"hello": value}
    module.exit_json(changed=False, meta=response)

if __name__ == "__main__":
    main()