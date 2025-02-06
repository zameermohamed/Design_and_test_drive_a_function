# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(age:str):
    """Checks an inputted DOB to see if the user is old enough and either grants or denies access. 

    Parameters: (list all parameters and their types)
        age: a string in format 'YYYY-MM-DD

    Returns: (state the return value and its type)
        an access granted message ("Accesss granted!")
        an access denied message, ("Access denied. Your current age is 'AGE' and required age is 16.")
        Error-message if DOB is provided in the wrong format 

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
Given a DOB over 16
It returns a string saying 'Access granted!'
"""
def test_age_checker_over_sixteen():
    assert age_checker("2000-01-01") == 'Access granted!'
    
"""
Given a DOB under 16
It returns a string saying 'Access denied!' Your current age is 'AGE' and required age is 16."
"""
def test_age_checker_under_sixteen():
    assert age_checker("2024-01-01") == "Access denied. Your current age is 1 and required age is 16."

"""
Given a DOB 16 today
It returns a string saying 'Access granted!'
"""
def test_age_checker_exactly_sixteen():
    assert age_checker("2009-06-02") == "Access granted!"

"""
Given a DOB that is in the incorrect format 
It returns an error message "Incorrect date of birth format" 
"""
def test_age_checker_incorrect_dob_format():
    with pytest.raises(Exception) as e:
        age_checker("01-01-2024") 
    error_message = str(e.value)
    assert error_message = "Incorrect date of birth format"
```

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
