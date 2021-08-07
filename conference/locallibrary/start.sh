#!/bin/sh
pip install -r requirements.txt
python3 manage.py makemigration
python3 manage.py migrate
echo "Successful migration"

python3 manage.py loaddata catalog/presentation.json
python3 manage.py loaddata catalog/room.json

python3 manage.py runserver
echo "Server is run"
