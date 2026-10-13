from lib.includes_todo import *

def test_true_when_todo_at_start():
    result = includes_todo('#TODO buy milk')
    assert result == True

def test_when_invalid():
    result = includes_todo("drink tea")
    assert result == False

def test_true_when_todo_at_end():
    result = includes_todo("learn to test-drive my code #TODO")
    assert result == True