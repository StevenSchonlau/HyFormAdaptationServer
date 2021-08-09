apt-get update
apt-get install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl python3-django
apt-get install -y redis-server
apt-get install -y libhunspell-dev
pip3 install --upgrade pip
pip3 install gunicorn==20.0.4
pip3 install psycopg2-binary==2.8.6
pip3 install djangorestframework==3.12.2
pip3 install django-cors-headers==3.6.0
pip3 install channels==2.4.0
pip3 install channels_redis==3.2.0
pip3 install Django==3.1.4
pip3 install ortools==8.1.8487
pip3 install bleach==3.2.1
pip3 install grpcio==1.34.0
pip3 install pandas==1.1.5
pip3 install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip3 install tabulate==0.8.7
pip3 install celery==5.1.2
pip3 install redis==3.5.3
pip3 install nltk==3.5
pip3 install hunspell==0.5.5
pip3 install scikit-learn==0.24.1
pip3 install websocket-client==1.1.0
pip3 install lark==0.11.3 
sudo -u postgres psql -f /vagrant/psql-script
mkdir /usr/share/ateams_service
cp -r /vagrant/evaluation /usr/share/ateams_service
mkdir /usr/share/ateams_data
cp -r /vagrant/nltk_data /usr/share/ateams_data
useradd celery
mkdir /etc/conf.d
cp /vagrant/celery/celery /etc/conf.d/celery
cp /vagrant/celery/celery.conf /etc/tmpfiles.d/celery.conf
cp /vagrant/celery/celery.service /etc/systemd/system/celery.service
systemd-tmpfiles --create
systemctl daemon-reload
systemctl enable celery.service
systemctl start celery.service
