#!/bin/bash

OS=$(uname -a)
AWS_CLI=$(aws --version)

echo "{\"changed\":false,\"kernal version\":\"$OS\",\"AWS CLI version\":\"$AWS_CLI\"}"