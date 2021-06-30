#!/bin/bash

UNIX_VERSION=$(uname -a)
AWS_CLI_VERSION=$(aws --version 2>&1 | cut -d " " -f1 | cut -d "/" -f2)

echo "{\"changed\":false,\"System Information\":\"$UNIX_VERSION\",\"AWS CLI version\":\"$AWS_CLI_VERSION\"}"