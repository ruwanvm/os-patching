#!/usr/bin/python

import os
import getpass

from PyInquirer import style_from_dict, Token, prompt

def main():
    print('{} starting OS Patching'.format(getpass.getuser()))

if __name__ == '__main__':
    main()