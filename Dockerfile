FROM python:3.7

ENV DJANGO_CONFIGURATION Docker

WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn_conf.py", "--chdir", "nddapp", "nddapp.wsgi:application", "--reload"]
