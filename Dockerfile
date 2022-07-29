FROM python:3.8-slim-buster
WORKDIR /Users/kirandarshak/Documents/Work_Project
ADD Q1.py .
ADD integral-tensor-307421-01d7f5c42a18.json .


COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./Q1.py" ] 
