# python-django-rest
This is my lab for thinkering with Django Rest Framework.

## Requirements

At the time I made this, I used Python 3.12 and the following versions:
```bash
asgiref==3.7.2
astroid==3.1.0
colorama==0.4.6
dill==0.3.8
Django==5.0.3
django-filter==24.1
djangorestframework==3.14.0
Faker==24.1.0
isort==5.13.2
lazy-object-proxy==1.10.0
Markdown==3.5.2
mccabe==0.7.0
platformdirs==4.2.0
pylint==3.1.0
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
sqlparse==0.4.4
tomlkit==0.12.4
tzdata==2024.1
validate-docbr==1.10.0
```

If you wish to install the same versions, do
```bash
pip install -r requirements.txt
```
But I always encourage using the latest version. If errors occur, at least you learn how to debug and work with the updated modules. To do so, do the following command (any required dependencies should be installed as well):
```bash
pip install django djangorestframework django-filter Faker markdown pylint validate-docbr
```
## The APIs
I might add different apps overtime. At the moment that are two: "clientes" and "escola".
> Since this is for practicing, I am using the same django project for all the apps - ```setup```(still not sure if this will change).

### Escola
This app simulates a school in which we can have students and courses. Students may be enrolled in courses.

### Clientes
This app simulates clientes database of some business. This API simply interacts with the db, being possible to add clients, edit or delete them.

## Usage
In order the start the Django Rest framework, make sure to be in the inner ```setup``` directory (not the one that contains ```README.md``` and ```requirements.txt```) and:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
The 2 previous commands will handle the db creation.

Populate the database (if you do not wish to add data manually)
```bash
python populate_db.py
```
Finally:
```bash
python manage.py runserver
```

> ⚠ some of the text within the apps and settings is in pt-br due to my instructor being Brazilian. Should not be a problem and I might refactor this sometime.