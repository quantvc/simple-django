#!/bin/bash

python manage.py syncdb --settings=quantvc.settings.dev --noinput
python manage.py migrate --settings=quantvc.settings.dev
python manage.py collectstatic --settings=quantvc.settings.dev --noinput