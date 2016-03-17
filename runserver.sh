#APP_CONFIG = 'path to config'
sudo mkdir -p /var/log/gunicorn
sudo nginx -s reload
sudo gunicorn -c gun.conf app:app
