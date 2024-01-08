from . import app
from data.tasks import tasks_list


@app.route('/')
def index():
    return f"Hello, please search for a task"

@app.route('/tasks')
def get_tasks():
    tasks = tasks_list
    return tasks


@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task = tasks_list
    for task in task:
        if task['id'] == task_id:
            return task
    return