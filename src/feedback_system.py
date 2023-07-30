```python
from flask import Flask, request, jsonify
from src.database_manager import manage_database
from src.ai_models import train_ai_model

app = Flask(__name__)

feedback_data = []

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    feedback = request.get_json()
    feedback_data.append(feedback)
    manage_database('feedback', feedback_data)
    train_ai_model(feedback_data)
    return jsonify({'message': 'feedback_submission_success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```