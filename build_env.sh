#!/bin/bash
echo $0: Creating virtual environment
virtualenv --prompt="<gallery>" ./env

mkdir ./logs
mkdir ./pids

echo $0: Installing dependencies
source ./env/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
./env/bin/pip install --requirement=./requirements.pip --log=./logs/build_pip_packages.log

echo $0: Making virtual environment relocatable
virtualenv --relocatable ./env

echo $0: Creating virtual environment finished.