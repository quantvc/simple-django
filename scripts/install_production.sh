#!/bin/bash

mysql -u root -e " CREATE DATABASE IF NOT EXISTS quantvc DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"
# python3.4 ./web/manage.py makemigrations --settings=quantvc.settings.product
python3.4 ./web/manage.py syncdb --settings=quantvc.settings.product --noinput
python3.4 ./web/manage.py collectstatic --settings=quantvc.settings.product --noinput --clear
python3.4 ./web/manage.py check --settings=quantvc.settings.product