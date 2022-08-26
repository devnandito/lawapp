import multiprocessing

bind = 'unix:/var/www/venv/lawapp/run/gunicorn.sock'
workers = multiprocessing.cpu_count() * 2