FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install -r requirements.txt
