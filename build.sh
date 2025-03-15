#!/bin/bash
echo "Starting build process..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate --noinput





echo "Build process completed successfully!"

