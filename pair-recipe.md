## The Problem
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## Function
``` python
def includes_todo(notes):
#Parameters
# Notes is a string representing my tasks
#Return
#Boolean 
```

## Examples
``` python

>>> includes_todo("#TODO buy milk")
True

>>> includes_todo("drink tea")
False

>>> includes_todo("learn to test-drive my code #TODO")
True

```