 FROM python:3.8-alpine
 MAINTAINER test1 test2 test3 test4

 ENV PYTHONUNBUFFERED 1

 COPY ./requirements.txt /requirements.txt
 RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
 RUN pip install -r /requirements.txt

 RUN mkdir /Copyrka
 WORKDIR /Copyrka
 COPY ./Copyrka /Copyrka

 RUN adduser -D sasha
 USER sasha

