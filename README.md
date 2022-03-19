# Book Store API
A Django RESTful API
### Installation
First, clone the repo:
```bash
$ git clone git@github.com:hasib32/book-store-api.git
$ cd book-store-api
```
Set `settings.py`
```bash
$ app/example_settings.py > app/settings.py
```

You have two options to run the application
1. Using Docker
```bash
$ docker-compose up -d
```
```bash
First, you need to go inside docker container

$ docker exec -it book-store-api bash
$ python manage.py migrate
$ python manage.py createsuperuser # Follow the steps
```
2. Without Docker

Make sure to change your default `database` in settings.py to `sqlite`
```bash
$ pipenv install # If you don't have pipenv install. please install it first.
$ python manage.py migrate
$ python manage.py createsuperuser # Follow the steps
$ python manage.py runserver
```
You should be able to access the API http://127.0.0.1:8000
### Using the API Endpoints
All the endpoints are protected using Django [TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication).
So, first you need to obtain a token.

#### Token endpoint
Method | Endpoint | Request Body
--- | --- | ---
POST | `/api-token-auth/` | {username, password}

#### API Endpoints:
Method | Endpoint | Functionality | Filter Params | Ordering
--- | --- | --- | --- | ---
POST | `/users/` | Create an User| N/A | N/A
POST | `/users/` | Get list of Users | N/A | N/A
GET | `/users/{id}` | Get an User Details | N/A | N/A
GET | `/users/me` | Get auth User | N/A | N/A
POST | `/library/` | Create a Library | N/A | N/A
GET | `/library/` | Get list of Library | N/A | N/A
GET | `/library/{id}` | Get a Library Details | N/A | N/A
POST | `/books/` | Create a Book | N/A | N/A
GET | `/books/` | Get list of Books  | N/A | N/A
GET | `/books/{id}` | Get a Book Details  | N/A | N/A
GET | `/library/{id}/books` | Get all the books for the Library  | `author,status` | `title,author`
POST | `/transactions/` | Create a Transactions | N/A | N/A
GET | `/transactions/` | Get list of Transactions | `due_date,book_id` | `due_date`
GET | `/transactions/{id}` | Get a Transactions Details | N/A | N/A
GET | `/users/{id}/books` | Users rented books past and current | `due_date,status` | `due_date`
