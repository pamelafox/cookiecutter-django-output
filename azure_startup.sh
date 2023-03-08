python manage.py migrate
python manage.py collectstatic --no-input
celery -A config.celery_app worker --loglevel=info --detach --uid=65534 -B
python -m gunicorn --workers 2 --threads 1 --timeout 60 --access-logfile \'-\' --error-logfile \'-\' --bind=0.0.0.0:8000 --chdir=/home/site/wwwroot config.wsgi
