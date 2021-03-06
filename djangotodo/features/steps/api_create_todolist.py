import json
from behave import given, when, then


@given(u'an endpoint for creating a list exists')
def step_impl(context):
    response = context.test.client.post('/api/lists/', data={})
    response_content = response.content.decode('utf-8')
    assert response_content == '{"name":["This field is required."],"description":["This field is required."]}'


@when(u'I send a payload with the name as "Homework to do" '
      u'and a description as "A list of homework tasks to do"')
def step_impl(context):
    response = context.test.client.post('/api/lists/', {
        "name": "Homework to do",
        "description": "A list of homework tasks to do"
    })
    response_dict = json.loads(response.content.decode('utf-8'))
    context.list_id = response_dict.get('id')
    assert response_dict.get('name') == 'Homework to do'
    assert response_dict.get('description') == 'A list of homework tasks to do'


@then(u'a list with the name "Homework to do" and '
      u'description "A list of homework tasks to do" should be created')
def step_impl(context):

    url = '/api/lists/{list_id}/'.format(list_id=context.list_id)
    response = context.test.client.get(url)
    assert response.status_code == 200

    try:
        response_dict = json.loads(response.content)
    except ValueError as e:
        response_dict = []
        print(e)
        print("content: " + response.content)

    assert response_dict.get('name') == 'Homework to do'
    assert response_dict.get('description') == 'A list of homework tasks to do'


@when(u'I send a payload with the name as "Errands to run" '
      u'and a description as "A list of errands to run"')
def step_impl(context):
    response = context.test.client.post('/api/lists/', {
        "name": "Errands to run",
        "description": "A list of errands to run"
    })
    response_dict = json.loads(response.content.decode('utf-8'))
    context.list_id = response_dict.get('id')
    assert response_dict.get('name') == 'Errands to run'
    assert response_dict.get('description') == 'A list of errands to run'


@then(u'a list with the name "Errands to run" and '
      u'description "A list of errands to run" should be created')
def step_impl(context):

    url = '/api/lists/{list_id}/'.format(list_id=context.list_id)
    response = context.test.client.get(url)

    try:
        response_dict = json.loads(response.content)
    except ValueError as e:
        response_dict = []
        print(e)
        print("content: " + response.content)

    assert response_dict.get('name') == 'Errands to run'
    assert response_dict.get('description') == 'A list of errands to run'
