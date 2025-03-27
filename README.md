# Setup

1. Make migration
````
python 5_rest_api/manage.py makemigrations
````

2. migrate
````
python 5_rest_api/manage.py migrate
````

3. craete super user
````
python 5_rest_api/manage.py createsuperuser
````
create password

4. start server
````
python 5_rest_api/manage.py runserver
````

admin local server >>>> http://localhost:8000/admin/ 
api local server >>>> http://127.0.0.1:8000/api/schools/