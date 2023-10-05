# hackathon-flask-bakend

virtualenv venv -p python3.9.13
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

gunicorn application:application