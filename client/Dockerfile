FROM python:3.8

RUN mkdir /client/
RUN pip install requests

WORKDIR /client/

COPY  . /client/

CMD [ "python", "client.py" ]