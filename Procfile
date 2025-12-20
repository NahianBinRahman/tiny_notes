web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn tiny_notes.wsgi:application --bind 0.0.0.0:$PORT
