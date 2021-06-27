FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/soyolim-txter/SOYOLIM.git

WORKDIR /home/SOYOLIM/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-)02_#9l&0slyqvuf3zne6l3d!v)$ud2*9j3)mob(w@&m&)!w(+" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=SOYOLIM.settings.deploy && gunicorn SOYOLIM.wsgi --env DJANGO_SETTINGS_MODULE=SOYOLIM.settings.deploy --bind 0.0.0.0:8000"]
