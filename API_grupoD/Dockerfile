FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python manage.py makemigrations --settings=grupo_d.settings.dev_sqlite
RUN python manage.py migrate --settings=grupo_d.settings.dev_sqlite
