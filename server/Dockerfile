FROM python:3.8

RUN mkdir server
RUN pip install flask

WORKDIR /server/

COPY  . /server/

CMD [ "python", "server.py" ]
