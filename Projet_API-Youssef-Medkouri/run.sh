#!/usr/bin/env bash
touch db.sqlite3
docker rm -f restaurant &>/dev/null && echo 'Removed old container'
docker run -v $(pwd)/db.sqlite3:/app/db.sqlite3 -e PORT=8000 \
-e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_EMAIL=admin@example.com -e DJANGO_SUPERUSER_PASSWORD=admin \
--name restaurant -it api