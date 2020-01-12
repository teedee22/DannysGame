Provisioning a new site
=======================
eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/danniesgame.com/g" \
    | sudo tee /etc/nginx/sites-available/danniesgame.com

    sudo ln -s /etc/nginx/sites-available/danniesgame.com \
    /etc/nginx/sites-enabled/danniesgame.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/danniesgame.com/g" \
    | sudo tee /etc/systemd/system/danniesgame.com.service

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
