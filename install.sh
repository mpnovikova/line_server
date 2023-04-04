#! /bin/bash

pyenv virtualenv line_server
pyenv activate line_server
pip3 install --upgrade pip
pip3 install -r requirements.txt

