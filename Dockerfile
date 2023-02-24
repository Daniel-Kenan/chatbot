FROM python:3.6.13

WORKDIR /app

COPY . /app
RUN pip install tensorflow
RUN pip install numpy
RUN pip install websockets
RUN pip install nltk

EXPOSE 8765
CMD python ./server.py 
