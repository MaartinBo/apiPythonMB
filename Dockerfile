FROM python:latest

MAINTAINER testDockerPythonApi

RUN mkdir /automation

RUN apt-get update && apt-get -y install vim

COPY ./mbtest /automation/mbtest
COPY ./requirements.txt /automation

WORKDIR /automation

RUN pip install -r requirements.txt
