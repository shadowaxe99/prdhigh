```python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TaskAPI(Resource):
    def get(self, task_id):
        # Fetch task from database
        task = manage_database('get', task_id)
        if not task:
            return {'error': 'Task not found'}, 404
        return task

    def put(self, task_id):
        # Update task in database
        task_data = request.get_json()
        result = manage_database('update', task_id, task_data)
        return result

    def delete(self, task_id):
        # Delete task from database
        result = manage_database('delete', task_id)
        return result

class TaskListAPI(Resource):
    def get(self):
        # Fetch all tasks from database
        tasks = manage_database('get_all')
        return tasks

    def post(self):
        # Create new task in database
        task_data = request.get_json()
        result = manage_database('create', task_data)
        return result

api.add_resource(TaskListAPI, '/tasks')
api.add_resource(TaskAPI, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
```