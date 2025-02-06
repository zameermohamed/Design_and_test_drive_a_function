from lib.age_checker import age_checker
import pytest

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
    assert age_checker("2009-02-06") == "Access granted!"

"""
Given a DOB that is in the incorrect format 
It returns an error message "Incorrect date of birth format" 
"""
def test_age_checker_incorrect_dob_format():
    with pytest.raises(Exception) as e:
        age_checker("01-01-2024") 
    error_message = str(e.value)
    assert error_message == "Incorrect date of birth format"


def test_age_checker_incorrect_dob_format_two():
    with pytest.raises(Exception) as e:
        age_checker("birthday") 
    error_message = str(e.value)
    assert error_message == "Incorrect date of birth format"

def test_age_checker_future_date():
    with pytest.raises(Exception) as e:
        age_checker("2026-01-01") 
    error_message = str(e.value)
    assert error_message == "Date of birth is in the future!"