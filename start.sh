#!/bin/bash
cd GearForRide
python manage.py collectstatic --noinput
gunicorn GearForRide.wsgi