from behave import given, when, then


@given(u'an endpoint for creating a list exists')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an endpoint for creating a list exists')


@when(u'I send a payload with the name as "Homework to do" '
      u'and a description as "A list of homework tasks to do"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a payload with the name '
                              u'as "Homework to do" and a description as '
                              u'"A list of homework tasks to do"')


@then(u'a list with the name "Homework to do" and '
      u'description "A list of homework tasks to do" should be created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a list with the name "Homework to do" and '
                              u'description "A list of homework tasks to do" '
                              u'should be created')


@when(u'I send a payload with the name as "Errands to run" '
      u'and a description as "A list of errands to run"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a payload with the name as "Errands to run" '
                              u'and a description as "A list of errands to run"')


@then(u'a list with the name "Errands to run" and '
      u'description "A list of errands to run" should be created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a list with the name "Errands to run" and '
                              u'description "A list of errands to run" should be created')
