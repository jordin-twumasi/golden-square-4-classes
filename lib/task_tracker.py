class TaskTracker:
    def __init__ (self):
        self.list_incomplete = []

    def add(self, task):
        # Parameters:
        # String - reps task to be added
        self.list_incomplete.append(task)

    def list_incomplete_tasks(self):
       # Returns:
       # List of all items in todo

       return self.list_incomplete


    def mark_complete(self, task_index):
       # Parameters - task with ibdex?
       # Side Effects
       # Item removed from list 
       if task_index >= len(self.list_incomplete):
           raise Exception("You cannot mark complete a task that does not exist.")
       else:
         self.list_incomplete.pop(task_index)
