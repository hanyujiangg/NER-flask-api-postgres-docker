# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm
RUN pip install -U nltk
RUN python -c "import nltk;nltk.download('FreqDist')"

COPY . .

CMD [ "python", "flask_api.py"]
