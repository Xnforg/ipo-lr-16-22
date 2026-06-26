#!/bin/bash

# НЕ НУЖЕН cd, так как manage.py уже в /app/
# Если start.sh в корне с manage.py, то cd не нужен

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn GearForBikes.wsgi:application --bind 0.0.0.0:8080