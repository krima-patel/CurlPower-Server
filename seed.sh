#!/bin/bash
rm -rf curlpowerapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations curlpowerapi
python manage.py migrate curlpowerapi
python manage.py loaddata users
python manage.py loaddata routines
python manage.py loaddata products
python manage.py loaddata hairtypes
python manage.py loaddata producthairtypes

# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
