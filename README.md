# django-tute

Django tutorials

### base

```
mkdir -p django-tute
cd django-tute
virtualenv -p /usr/local/bin/python3 .venv
source .venv/bin/activate
which python
which pip
pip list
pip install django==2.2
python -m django --version
```

---

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

### create a project

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
cd aasite 
python manage.py runserver
(CTRL+C)
cd ..
```

### create a project then create an app

```
django-admin startproject absite
cd absite
python manage.py startapp polls
python manage.py runserver
```

---

