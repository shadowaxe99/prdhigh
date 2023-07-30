```python
import os
from ai_models import AIModel

class CodeProcessingAgent:
    def __init__(self):
        self.ai_model = AIModel()

    def process_code(self, code_file_path):
        if not os.path.exists(code_file_path):
            raise Exception(f"File {code_file_path} does not exist")

        with open(code_file_path, 'r') as code_file:
            code_content = code_file.read()

        processed_code = self.ai_model.process_code(code_content)

        return processed_code
```