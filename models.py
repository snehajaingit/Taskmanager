class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['description'], data['due_date'], data['completed'])


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            'name': self.name,
            'tasks': [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        project = Project(data['name'])
        project.tasks = [Task.from_dict(t) for t in data['tasks']]
        return project
