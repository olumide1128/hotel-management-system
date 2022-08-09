release: python manage.py migrate
web: gunicorn hotel_mgt_system.wsgi --log-file - --log-level debug --preload --workers 1
