#!/bin/bash
echo "Starting build process..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Collect static files (important for production)
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000

echo "Build process completed successfully!"

