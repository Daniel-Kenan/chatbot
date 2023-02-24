FROM python:3.6.8-alpine3.8

RUN pip install tensorflow
RUN pip install numpy
RUN pip install websockets
RUN pip install nltk

COPY . .

CMD ["python", "server.py"]