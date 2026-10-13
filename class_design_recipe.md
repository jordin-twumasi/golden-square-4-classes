## The Problem
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## Class Interface

``` python
class TaskTracker:
    def add(self, task):
        # Parameters:
        # String - reps task to be added
        pass

    def list_incomplete_tasks(self):
       # Returns:
       # List of all items in todo

       pass


   def mark_complete():
       # Parameters - task with ibdex?
       # Side Effects
       # Item removed from list 
       pass
```

## Examples 
```python
"""
Initially there are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete => []



"""
Adding a new task,
 updates tracker to be displayed in list of tasks
"""
tracker = TaskTracker()
tracker.add('Wash the dishes')
tracker.list_incomplete => ['Wash the dishes']

"""
Adding another task,
 updates tracker to be displayed in list of tasks
"""
tracker = TaskTracker()
tracker.add('Wash the dishes')
tracker.add('Take out the bins')
tracker.list_incomplete => ['Wash the dishes', 'Take out the bins']


"""
Marking a task as complete
Task disappears from list
"""
tracker = TaskTracker()
tracker.add('Wash the dishes')
tracker.add('Take out the bins')
tracker.mark_complete(1)
tracker.list_incomplete => ['Wash the dishes']


"""
Marking a task as complete that doesnt exist
Raise an error
"""
tracker = TaskTracker()
tracker.add('Wash the dishes')
tracker.add('Take out the bins')
tracker.mark_complete(2) #Raises an error


```