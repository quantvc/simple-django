#!/bin/bash

# create dir
mkdir /home/web/
mkdir /home/web/website/
mkdir /home/web/logs/
mkdir /home/web/static/
mkdir /home/web/media/

# packages
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
sudo apt-get install python3.4 python3.4-dev libmysqlclient-dev mysql-server-core-5.6 libevent-dev libjpeg-dev zlib1g-dev libpng12-dev
sudo apt-get install libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
sudo apt-get install python3-setuptools
sudo apt-get install git-core
sudo apt-get install redis-server redis-tools
sudo apt-get install nginx
sudo apt-get install libpcre3-dev
sudo easy_install3 pip
sudo pip3 install virtualenvwrapper

# virtulenv
# create the virtulenv path
mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs

sudo "VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3" >> ~/.bashrc
sudo "source /user/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc
# create virtulenv python3 env
mkvirtualenv web

# python packages

chmod +x ./scripts/pip.sh

./pip.sh

# website  deploy
chmod +x ./scripts/install_production.sh
./install_production.sh

# redis

sudo redis-server config/redis.conf


# nginx
sudo service nginx stop
sudo cp ./conf/web_nginx  /etc/nginx/sites-avalilable/

sudo ln -s  /etc/nginx/sites-avalilable/web_nginx /etc/nginx/sites-enabled/web_nginx
sudo service nginx restart

# uwsgi

uwsgi --ini ./conf/uwsgi.ini











