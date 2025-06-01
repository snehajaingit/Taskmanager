import json
from models import Task

def save_tasks(tasks, filename='data/tasks.json'):
    with open(filename, 'w') as f:
        json.dump([{
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'completed': task.completed
        } for task in tasks], f, indent=4)

def load_tasks(filename='data/tasks.json'):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            return [Task(
                title=t['title'],
                description=t['description'],
                due_date=t['due_date'],
                completed=t.get('completed', False)
            ) for t in tasks_data]
    except FileNotFoundError:
        return []
