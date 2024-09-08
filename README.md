# django-tute

Django tutorials

### Prerequisite

```
mkdir -p django-tute
cd django-tute

python3 -m venv .venv
source .venv/bin/activate

pip install Django
python -m django --version
5.1.1
```

## Getting Started

- https://docs.djangoproject.com/en/5.1/intro/tutorial01/

### Create a Django project

```
which django-admin
django-admin startproject aasite
tree aasite
aasite
├── aasite
│   ├── __init__.py
│   ├── asgi.py
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

- https://docs.djangoproject.com/en/5.1/ref/applications/

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

```
pip install djangorestframework
```

```
python -c "import rest_framework; print(rest_framework.VERSION)"
3.15.2
```

### Django REST quickstart

- https://www.django-rest-framework.org/tutorial/quickstart/

```
django-admin startproject zzrest
cd zzrest/zzrest
django-admin startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver

curl -H "Accept: application/json; indent=4" -u admin:123456 http://127.0.0.1:8000/users/
curl -s http://127.0.0.1:8000/users/ | jq
open -a Safari http://127.0.0.1:8000
```

### Django REST with auth

- https://www.django-rest-framework.org/api-guide/permissions/
- https://www.django-rest-framework.org/api-guide/authentication/
- https://www.django-rest-framework.org/topics/documenting-your-api/

```
django-admin startproject zzrestauth
cd zzrestauth/zzrestauth
django-admin startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```

Auth Token
```
python manage.py drf_create_token --help

python manage.py drf_create_token admin
Generated token d1ec2c19f942ad9e8a9c836cc4319927cbe59f7e for user admin

curl -s -X GET http://localhost:8000/users/ -H "Authorization: Token d1ec2c19f942ad9e8a9c836cc4319927cbe59f7e" | jq
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
```

Get token by using username and password
```
curl -s -X POST -d '{"username": "admin", "password": "123456"}' -H "Content-Type: application/json" "http://localhost:8000/api-token-auth/" | jq
{
  "token": "d1ec2c19f942ad9e8a9c836cc4319927cbe59f7e"
}
```

You also can manage tokens through admin console
- http://localhost:8000/admin/authtoken/tokenproxy/

API Documentation
- https://drf-spectacular.readthedocs.io/en/latest/readme.html

```
pip install drf-spectacular
```

```
python manage.py spectacular --help
python manage.py spectacular --format openapi-json | jq
python manage.py spectacular | yq
python manage.py spectacular | yq > openapi.yaml
```

- http://localhost:8000/api/schema/swagger-ui/
- http://localhost:8000/api/schema/redoc/
