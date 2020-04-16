FROM python:3.8

RUN apt-get update && apt-get install -yy gcc build-essential python-setuptools

ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

CMD python app.py