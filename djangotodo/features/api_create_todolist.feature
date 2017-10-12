Feature: create a Todo list via the api
  As an api client
  I want to be able to create a Todo list

  Scenario Outline: create list that does not exist
    Given an endpoint for creating a list exists
    When I send a payload with the name as "<name>" and a description as "<description>"
    Then a list with the name "<name>" and description "<description>" should be created

    Examples:
      | name                    | description                               |
      | Homework to do          | A list of homework tasks to do            |
      | Errands to run          | A list of errands to run                  |