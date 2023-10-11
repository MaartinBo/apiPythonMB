FROM python:latest

MAINTAINER testDockerPythonApi

RUN mkdir /automation

RUN apt-get update && apt-get -y install vim

COPY ./mbtest /automation/mbtest
COPY ./setup.py /automation

WORKDIR /automation

RUN pip install .
