# hackathon-flask-bakend

virtualenv venv -p python3.9
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
gunicorn application:application