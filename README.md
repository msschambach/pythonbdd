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

To write BDD test, we first describe a feature using a [gherkin](http://pythonhosted.org/behave/gherkin.html#chapter-gherkin) file. For example, to test a new feature, you'd create a `new_feature.feature` file in `pythonbdd/djangotodo/features`. A simple example would look like:
```
# new_feature.feature
Feature: feature name

  Scenario: some scenario
      Given some condition
       Then some result is expected
```

Then run
```
python manage.py behave --settings=configuration.settings.test
```

You'll get an output which contains the following:
```
You can implement step definitions for undefined steps with these snippets:

@given(u'some condition')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given some condition')

@then(u'some result is expected.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then some result is expected.')
```

This is to be used as a reference to create your steps file. So in `pythonbdd/djangotodo/features/steps` create a file named `new_feature.py`
with the following content:
```
"""
new_feature.py
This is where you implement the tests for the feature.
"""
from behave import given, when, then

@given(u'some condition')
def step_impl(context):
    # implement test here

@then(u'some result is expected.')
def step_impl(context):
    # implement test here
```

Once you implement the tests, you can then run
```
python manage.py behave --settings=configuration.settings.test
```
again.

For reference have a look at `pythonbdd/djangotodo/features/api_create_todolist.feature`  and `pythonbdd/djangotodo/features/steps/api_create_todolist.py`

NB: If you create a gherkin file called `example.feature`, the steps file must be called `example.py`.

For more reference, you can have a look at:

* [Introduction to BDD in python](https://www.merixstudio.com/blog/behavior-driven-development-python/)

* [Tuts plus Tutorial on BDD in python](https://code.tutsplus.com/tutorials/behavior-driven-development-in-python--net-26547)

* [Beginning BDD with Django - Part One](http://whoisnicoleharris.com/2015/03/16/bdd-part-one.html)

* [Beginning BDD with Django - Part Two](http://whoisnicoleharris.com/2015/03/19/bdd-part-two.html)

* [Behave Reference on Gherkin](http://pythonhosted.org/behave/gherkin.html#chapter-gherkin)

* [BDD in pycharm](https://blog.jetbrains.com/pycharm/2017/06/upgrade-your-testing-with-behavior-driven-development/)




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
