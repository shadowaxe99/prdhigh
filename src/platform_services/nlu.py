```python
from openai import OpenAIGPT3

class NLUService:
    def __init__(self):
        self.model = OpenAIGPT3()

    def process_user_input(self, user_input):
        processed_input = self.model.process_input(user_input)
        return processed_input

    def extract_task(self, processed_input):
        task = self.model.extract_task(processed_input)
        return task

    def extract_parameters(self, processed_input):
        parameters = self.model.extract_parameters(processed_input)
        return parameters
```