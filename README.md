# django-tute

Django tutorials

### Prerequisite

```
mkdir -p django-tute
cd django-tute

python3 -m pip install virtualenv
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
(venv) which python
(venv) which pip
(venv) pip list
(venv) pip install django==2.2
(venv) python -m django --version
(venv) deactivate
```

## Getting Started

- https://docs.djangoproject.com/en/2.2/intro/tutorial01/

### Create a Django project

```
which django-admin
django-admin startproject aasite
tree aasite
aasite
├── aasite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
pushd aasite 
python manage.py runserver
(CTRL+C)
popd
```

### Create a Django project then create a Django app

```
django-admin startproject absite
pushd absite
python manage.py startapp polls
python manage.py runserver
(CTRL+C)
popd
```

#### Understanding Django project and application

- https://docs.djangoproject.com/en/2.2/ref/applications/

```
pushd absite
python manage.py shell
>>> from django.apps import apps
>>> apps.get_app_config('admin').verbose_name
'Administration'
>>> apps.get_app_config('polls').verbose_name
'Polls'
>>> apps.get_app_configs()
>>> exit()
popd
```

## Django REST Framework

### Django REST quickstart

- https://www.django-rest-framework.org/tutorial/quickstart/

```
pip install djangorestframework
django-admin startproject zzrest
cd zzrest/zzrest
django-admin startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver

curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
curl -s http://127.0.0.1:8000/users/ | jq
open -a Safari http://127.0.0.1:8000
```

Generating an OpenAPI Schema
- https://www.django-rest-framework.org/api-guide/schemas/

```
pip install pyyaml
python manage.py generateschema > openapi-schema.yml

open -a Safari http://localhost:8000/openapi
```

### Django REST with auth

```
pip install -U 'drf-yasg[validation]'

django-admin startproject zzrestauth
cd zzrestauth/zzrestauth
django-admin startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```

API Document
```
open -a Safari http://localhost:8000
open -a Safari http://localhost:8000/swagger/
open -a Safari http://localhost:8000/redoc/

curl -s http://localhost:8000/swagger.json | jq
curl -s http://localhost:8000/swagger.yaml
```

Auth Token
```
open -a Safari http://localhost:8000/admin/authtoken/token/

curl -s -X GET http://localhost:8000/users/ | jq
{
  "detail": "Authentication credentials were not provided."
}

curl -s -X GET http://localhost:8000/users/ -H 'Authorization: Token f8f7ddc2f951663364cdc8c1c946c58d6d752ace' | jq
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "http://localhost:8000/users/1/",
      "username": "admin",
      "email": "admin@example.com",
      "groups": []
    }
  ]
}

python manage.py drf_create_token --help
```

Permissions
- https://www.django-rest-framework.org/api-guide/permissions/

Authentication
- https://www.django-rest-framework.org/api-guide/authentication/

Documenting your API
- https://www.django-rest-framework.org/topics/documenting-your-api/

Yet Another Swagger Generator (drf-yasg)
- https://github.com/axnsan12/drf-yasg/
