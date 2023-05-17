```python
from ai_models import AIModel

class AIAgentInteraction:
    def __init__(self):
        self.ai_model = AIModel()

    def interact_with_ai_agent(self, task_data):
        task_type = task_data['task_type']
        task_content = task_data['task_content']

        if task_type == 'git_clone':
            self.ai_model.git_operations(task_content)
        elif task_type == 'pdf_upload':
            self.ai_model.pdf_processing(task_content)
        elif task_type == 'code_upload':
            self.ai_model.code_processing(task_content)
        else:
            print("Invalid task type")

        return {'status': 'success', 'message': 'Task executed successfully'}
```