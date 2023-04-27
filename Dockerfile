FROM python:3.10.11-alpine3.17
WORKDIR /data
COPY . /snt
RUN pip install -r /snt/requirements.txt