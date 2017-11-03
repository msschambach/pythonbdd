# pythonbdd
An example of Behaviour Driven Development in python

## How to develop
* Clone repository: 
```
git clone https://github.com/msschambach/pythonbdd.git
```
* Install requirements:
```
cd pythonbdd/djangotodo
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
* To Run development server:
```
python manage.py runserver
```

## Testing

To run tests, make sure the virtual environment is activated then...
To run django tests run:
```
python manage.py test --settings=configuration.settings.test
```

To run BDD tests run:
```
python manage.py behave --settings=configuration.settings.test
```

## Tools, Libraries and Frameworks Used
* [Django](https://www.djangoproject.com/)
* [Behave](https://github.com/behave/behave)
* [Behave Django](https://github.com/behave/behave-django)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Django Extensions](https://github.com/django-extensions/django-extensions)


NB: Tested with python 2.7.10 and python 3.6.1
