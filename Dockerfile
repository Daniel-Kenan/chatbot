FROM alpine:latest
# FROM python:3.6.13

RUN apk add --no-cache --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

ADD . /opt/webapp/
WORKDIR /opt/webapp

RUN adduser -D myuser
USER myuser

CMD python gunicorn --bind 0.0.0.0:$PORT wsgi 
