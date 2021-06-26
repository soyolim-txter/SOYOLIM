FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/soyolim-txter/SOYOLIM.git

WORKDIR /home/SOYOLIM/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-)02_#9l&0slyqvuf3zne6l3d!v)$ud2*9j3)mob(w@&m&)!w(+" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "SOYOLIM.wsgi", "--bind", "0.0.0.0:8000"]
