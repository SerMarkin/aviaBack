FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && pip install gunicorn

RUN rm -r /root/.cache/pip && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD [ "gunicorn", "-c", "/app/aviaBack/gunicorn.py", "aviaBack.wsgi:application"]