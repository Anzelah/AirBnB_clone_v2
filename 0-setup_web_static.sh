#!/usr/bin/env bash
# Install nginx web server

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/ && sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current #remove if exists
sudo ln -s /data/web_static/releases/test/ /data/web_static/current #ln -s <target> <current>
sudo chown -R ubuntu: ubuntu /data/
sudo sed -i '61i \\tlocation \/hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
