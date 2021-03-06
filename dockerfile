FROM python:3.9.0a3-alpine3.10

ADD . /my-django-app

WORKDIR /my-django-app

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
