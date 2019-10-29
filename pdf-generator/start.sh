source devEnv/bin/activate
export APP_SETTINGS='config.cfg'
gunicorn --worker-class=gevent --worker-connections=1000 --workers=3 --bind 0.0.0.0:5000 wsgi:app
