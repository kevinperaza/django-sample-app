# django-sample-app

creating a new virtual env

```
python -m venv env-name
```

creating a new django project

```
django-admin startproject project-name
```

running django dev server

```
python manage.py runserver
```

create new "app"

```
python manage.py startapp app-name
```

See pending migrations

```
python manage.py showmigrations
```

Run django migrations

```
python manage.py migrate
```

Generate django migrations after updating a data model

```
python manage.py makemigrations
```

Inspect migration

```
python manage.py sqlmigrate app-name migration-name
```

Create super user to access django admin portal

```
python manage.py createsuperuser
```
