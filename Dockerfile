FROM python:3.9.0

WORKDIR /home/

RUN echo "testing5678"

RUN git clone https://github.com/soyolim-txter/SOYOLIM.git

WORKDIR /home/SOYOLIM/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=SOYOLIM.settings.deploy && python manage.py migrate --settings=SOYOLIM.settings.deploy && gunicorn SOYOLIM.wsgi --env DJANGO_SETTINGS_MODULE=SOYOLIM.settings.deploy --bind 0.0.0.0:8000"]
