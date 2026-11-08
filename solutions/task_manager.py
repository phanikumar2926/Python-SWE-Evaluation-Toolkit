class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty.")

        task = {
            "id": self.next_id,
            "description": description.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1

        return task["id"]

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True

        raise ValueError("Task not found.")

    def list_tasks(self):
        return [task.copy() for task in self.tasks]