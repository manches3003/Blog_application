#!/bin/bash
set -e

echo "Creating database tables..."
python -c "from app import create_app, db; app = create_app('production'); app.app_context().push(); db.create_all()"

echo "Starting gunicorn..."
exec gunicorn --bind 0.0.0.0:5000 --workers 2 "app:app"
