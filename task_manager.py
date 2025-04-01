import json
import time

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Upload the task from the json file."""
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    task.setdefault('in_process', False)
                    task.setdefault('time', 0)
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        """Save the tasks in the json file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task_name):
        """Add a new task."""
        self.tasks.append({"name": task_name, "status": "Incomplete", "time": 0, "in_process": False})
        self.save_tasks()

    def remove_task(self, index):
        """Delete a task by its index."""
        del self.tasks[index]
        self.save_tasks()

    def toggle_status(self, index):
        """Modify the status of a task."""
        task = self.tasks[index]
        task['status'] = "Complete" if task['status'] == "Incomplete" else "Incomplete"
        self.save_tasks()

    def start_task(self, index):
        """Start the chrono for the task."""
        self.tasks[index]['in_process'] = True
        self.save_tasks()

    def stop_task(self, index, elapsed_time):
        """Stop the chrono and display the time."""
        self.tasks[index]['time'] += elapsed_time
        self.tasks[index]['in_process'] = False
        self.save_tasks()

    def get_task(self, index):
        """Return to a specific task."""
        return self.tasks[index]

    def get_tasks(self):
        """return in the tasks."""
        return self.tasks
