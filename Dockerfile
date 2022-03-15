FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install pipenv

COPY ./Pipfile /Pipfile

RUN pipenv install --skip-lock --system --dev

COPY . /code/