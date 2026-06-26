#!/bin/bash
cd GearForBikes\GearForBikes
python manage.py collectstatic --noinput
gunicorn GearForBikes.wsgi