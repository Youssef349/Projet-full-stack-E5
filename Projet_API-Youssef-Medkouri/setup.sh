#!/usr/bin/env bash
touch db.sqlite3

docker exec restaurant ./manage.py migrate

docker exec restaurant ./manage.py createsuperuser --noinput