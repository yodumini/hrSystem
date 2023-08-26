FROM python:3.9
 
WORKDIR /app

ADD . /app

ENV FLASK_APP=API/app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt