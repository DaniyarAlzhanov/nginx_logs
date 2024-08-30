FROM python:3.9.10

WORKDIR /app

RUN pip install gunicorn==23.0.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ['gunicorn', '--bind', '0.0.0.0:8000', 'nginx_logs.wsgi']
