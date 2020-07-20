# EVO Project

### Installing

1. Firstly install requirements:

```
pip install -r requirements.txt
```

2. Then migrate migrations to db:

```
python manage.py migrate
```

3. Run project:

```
python manage.py runserver
```

4. And last, start task processing at another console:

```
python manage.py process_tasks
```

Now, you can use you app by link: http://localhost:8000/.






