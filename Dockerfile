from python:3.11-slim

workdir /app

copy requirements.txt .
run pip install --upgrade pip && pip install -r requirements.txt

copy . .

cmd ["gunicorn", "main_course.wsgi:application", "--bind", "0.0.0.0:8000"] 