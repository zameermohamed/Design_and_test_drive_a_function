# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user \
So that I can find my tasks among all my notes \
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def includes_todo(notes):
    """Informs user if #TODO is in notes

    Parameters: (list all parameters and their types)
        notes: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        boolean (True if #TODO is in notes)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string containing #TODO 
-> returns True
"""
def test_includes_todo_contains_TODO_only():
    assert includes_todo("#TODO")==True

def test_includes_todo_contains_TODO_at_end():
    assert includes_todo("some before #TODO")==True

def test_includes_todo_contains_TODO_at_begining():
    assert includes_todo("#TODO something after")==True

def test_includes_todo_contains_TODO_twice():
    assert includes_todo("#TODO #TODO")==True

"""
Given a string not containing #TODO 
-> returns False
"""

def test_does_not_include_todo_contains_TODO_only():
    assert includes_todo("TODO")==False

def test_does_not_include_todo_contains_TODO_at_end():
    assert includes_todo("some before TODO")==False

def test_does_not_include_todo_contains_TODO_at_begining():
    assert includes_todo("TODO something after")==False

"""
Given an empty string 
-> raise error "Can not check an empty string"
"""
def test_includes_todo_empty_string_raises_error()
with pytest.raises(Exception) as e:
    includes_todo()
error_message=str(e.value)
assert error_message=="Can not check an empty string"



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
