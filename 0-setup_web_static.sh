#!/usr/bin/env bash
# script thats sets up web servers for deployment of web_static

#install nginx if it is not installed
sudo apt-get install nginx

# create the folder /data/ if it doesnt exist
FOLDER_DATA=/data/
[ -d "$FOLDER_DATA" ] || sudo mkdir /data/

#Create the folder /data/web_static/ if it doesn’t already exist
FOLDER_WEBSTATIC=/data/web_static/
[ -d "$FOLDER_WEBSTATIC" ] || sudo mkdir /data/web_static/

#Create the folder /data/web_static/releases/ if it doesn’t already exist
FOLDER_RELEASES=/data/web_static/releases
[ -d "$FOLDER_RELEASES" ] || sudo mkdir /data/web_static/releases/

#Create the folder /data/web_static/shared/ if it doesn’t already exist
FOLDER_SHARED=/data/web_static/shared/
[ -d "$FOLDER_SHARED" ] || sudo mkdir /data/web_static/shared

#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
FOLDER_TEST=/data/web_static/releases/test/
[ -d "$FOLDER_TEST" ] || sudo mkdir /data/web_static/releases/test/

#create a fake html file with small content to be served
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | sudo tee /data/web_static/releases/test/index.html


# create a symbolic link to /data/web_static/releases/test/ folder
FILE_SYMLINK=/data/web_static/current
if [ -L "$FILE_SYMLINK" ]; then
    rm /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

#give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#update nginx configuration to serve content of /data/web_static/current/ to hbnb_static
sudo sed -i '74i\location /hbnb_static { alias /data/web_static/current;}' /etc/nginx/sites-available/default

sudo service nginx restart
