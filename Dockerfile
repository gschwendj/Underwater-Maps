# syntax=docker/dockerfile:1

FROM python:3.10-bullseye 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src ./src
COPY ./npy_data ./npy_data
COPY ./main.py .
CMD ["python3", "main.py"]