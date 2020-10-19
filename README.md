# suite5_test
First install python dependencies:

`pip install -r requirements.txt`

Start the docker mysql database:

`docker-compose up
`
Run the flask migration:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Start the flask server:

`python run.py`