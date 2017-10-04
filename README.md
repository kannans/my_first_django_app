# My First Django App

#### Install Django on MAC OS

```sh
sudo easy_install pip

sudo pip install virtualenv

virtualenv djang -p python3.6

cd djang

source bin/activate 

#(djang) pc114s-MacBook-Pro

pip install django==1.11.2
```

#### Create New Django Project & Run Django server

```sh
django-admin startproject my_first_django_app

# Intialize project with migration. It create basic Sqlite Database.

python manage.py migrate

# Run django server.

python manage.py runserver

# Django version 1.11.2, using settings 'my_first_django_app.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C
```

cheers!!
