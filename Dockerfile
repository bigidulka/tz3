FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]