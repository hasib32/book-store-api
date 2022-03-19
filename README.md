# Book Store API
A Django RESTful API
### Installation
First, clone the repo:
```bash
$ git clone git@github.com:hasib32/book-store-api.git
$ cd book-store-api
```
You have two options to run the application
1. Using Docker
```bash
$ docker-compose up -d
```
In-order to run migration we need to get inside docker container
```bash
$ docker exec -it book-store-api bash
$ python manage.py migrate
$ python manage.py createsuperuser # Follow the steps
```
2. Without Docker