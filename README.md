# django-sample-app

creating a new virtual env

```python
python -m venv env-name
```

creating a new django project

```python
django-admin startproject project-name
```

running django dev server

```python
python manage.py runserver
```

create new "app"

```python
python manage.py startapp app-name
```

See pending migrations

```python
python manage.py showmigrations
```

Run django migrations

```python
python manage.py migrate
```

Generate django migrations after updating a data model

```python
python manage.py makemigrations
```

Inspect migration

```python
python manage.py sqlmigrate app-name migration-name
```

Create super user to access django admin portal

```python
python manage.py createsuperuser
```
