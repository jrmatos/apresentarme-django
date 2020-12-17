# Apresentarme Django

## Instructions for running

### Install Python 3.7 and Pip

``sudo apt install python3.7``

``sudo apt install python3-pip``


### Virtualenv

``virtualenv -p /usr/bin/python3.7 env``

``source env/bin/activate``

### Install dependencies

``pip install -r requirements.txt``

### Sync database

``python manage.py migrate``

### Load fixtures

``python manage.py loaddata cards``

### Run server

``python manage.py runserver``

### Check if it is working

Go to http://127.0.0.1:8000/graphql and run this query:

```
query {
  allCards{
    id
    url
    name
    bio
    phone
  }
}
```

Check the image in docs/examples.png to see the examples.

## Admin

### Create super user

``python manage.py createsuperuser``

Go to http://127.0.0.1:8000/admin and login with your new user.

