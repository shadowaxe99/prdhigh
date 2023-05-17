```python
class KnowledgeBase:
    def __init__(self):
        self.knowledge = {}

    def add_knowledge(self, key, value):
        self.knowledge[key] = value

    def get_knowledge(self, key):
        return self.knowledge.get(key, None)

    def update_knowledge(self, key, value):
        if key in self.knowledge:
            self.knowledge[key] = value

    def delete_knowledge(self, key):
        if key in self.knowledge:
            del self.knowledge[key]
```