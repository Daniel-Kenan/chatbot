FROM python:3.6.13

WORKDIR /app

COPY . /app


RUN pip install websockets

EXPOSE 8765
CMD python ./prototype.py 
