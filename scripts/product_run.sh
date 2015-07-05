#!/usr/bin/env bash

sudo nginx -s reload

uwsgi --ini ./conf/uwsgi.ini