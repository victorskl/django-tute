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
