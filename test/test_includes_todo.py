from lib.includes_todo import includes_todo
import pytest

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
def test_includes_todo_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        includes_todo("")
    error_message=str(e.value)
    assert error_message=="Can not check an empty string"