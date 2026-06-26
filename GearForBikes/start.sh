#!/bin/bash

cd GearForRides

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn GearForBikes.wsgi:application --bind 0.0.0.0:8080