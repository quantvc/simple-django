#!/bin/bash

pip3.4 install -r requirements/base.txt --upgrade
pip3.4 install -r requirements/extension.txt --upgrade
pip3.4 install -r requirements/test.txt --upgrade
# macos CC=gcc pip3.4 install uwsgi
pip3.4 install uwsgi

