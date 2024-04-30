#!/bin/bash

set -e

COMMIT_HASH=`git rev-parse HEAD`

#npm run build --prefix myshop/myshop_front

export DJANGO_SETTINGS_MODULE=myshop.settings

cp -f .env myshop
cp -f requirements.txt myshop
cp -r unit_docker myshop

docker compose build --no-cache
docker compose up -d

#docker compose stop web-static
#docker compose rm --force web-static

docker compose exec -it web sh -c "python manage.py collectstatic"
docker compose exec -it web sh -c "python manage.py migrate"
docker compose exec -it web sh -c "python manage.py loaddata initial.json"
docker compose exec -it web sh -c "chown -R unit:unit media/"

rm myshop/.env
rm myshop/requirements.txt
rm -R myshop/unit_docker

echo "All done!"