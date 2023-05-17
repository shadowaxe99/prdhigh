```python
from flask import Flask, request, jsonify
from src.ai_orchestrator import orchestrate_ai_agents
from src.database_manager import manage_database

app = Flask(__name__)

@app.route('/execute_task', methods=['POST'])
def execute_task():
    task_data = request.get_json()
    task_type = task_data.get('task_type')
    task_content = task_data.get('task_content')

    # Validate task data
    if not task_type or not task_content:
        return jsonify({'message': 'Invalid task data'}), 400

    # Orchestrate AI agents to execute the task
    task_result = orchestrate_ai_agents(task_type, task_content)

    # Save task data and result to the database
    manage_database('save', 'TaskSchema', task_data)

    return jsonify({'task_result': task_result, 'message': 'Task execution successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```