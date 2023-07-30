```python
import openai

class AIModels:
    def __init__(self):
        self.gpt3_model = openai.GPT3()
        self.codex_model = openai.Codex()
        self.whisper_model = openai.Whisper()

    def train_gpt3_model(self, training_data):
        self.gpt3_model.train(training_data)

    def train_codex_model(self, training_data):
        self.codex_model.train(training_data)

    def train_whisper_model(self, training_data):
        self.whisper_model.train(training_data)

    def predict_gpt3(self, input_data):
        return self.gpt3_model.predict(input_data)

    def predict_codex(self, input_data):
        return self.codex_model.predict(input_data)

    def predict_whisper(self, input_data):
        return self.whisper_model.predict(input_data)
```