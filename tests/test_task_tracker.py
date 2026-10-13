from lib.task_tracker import TaskTracker
import pytest
"""
Initially there are no tasks
"""

def test_return_empty_list_when_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete_tasks()== [] 

"""
Adding a new task,
 updates tracker to be displayed in list of tasks
"""
def test_add_task_to_tracker_and_display_list():
    tracker = TaskTracker()
    tracker.add('Wash the dishes')
    assert tracker.list_incomplete_tasks() == ['Wash the dishes']

"""
Adding another task,
 updates tracker to be displayed in list of tasks
"""
def test_add_multiple_tasks_to_tracker_and_display_list():
    tracker = TaskTracker()
    tracker.add('Wash the dishes')
    tracker.add('Take out the bins')
    assert tracker.list_incomplete_tasks() == ['Wash the dishes', 'Take out the bins']


"""
Marking a task as complete
Task disappears from list
"""
def test_mark_task_complete_to_remmove_from_list():
    tracker = TaskTracker()
    tracker.add('Wash the dishes')
    tracker.add('Take out the bins')
    tracker.mark_complete(1)
    assert tracker.list_incomplete == ['Wash the dishes']


"""
Marking a task as complete that doesnt exist
Raise an error
"""
def test_mark_not_existing_task_complete_raise_error():
    tracker = TaskTracker()
    tracker.add('Wash the dishes')
    tracker.add('Take out the bins')
    with pytest.raises(Exception) as err:
        tracker.mark_complete(2) #Raises an error
    message = str(err.value)
    assert message == "You cannot mark complete a task that does not exist."