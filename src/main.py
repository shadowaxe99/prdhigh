```python
from flask import Flask, render_template, request, redirect, url_for
import src.user_authentication as ua
import src.task_execution as te
import src.ai_agent_interaction as ai
import src.feedback_system as fs
import src.database_manager as dm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_data = request.form
    if ua.authenticate_user(user_data):
        return redirect(url_for('task_selection'))
    else:
        return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    user_data = request.form
    ua.register_user(user_data)
    return redirect(url_for('home'))

@app.route('/task_selection', methods=['GET', 'POST'])
def task_selection():
    if request.method == 'POST':
        task_data = request.form
        te.execute_task(task_data)
        return redirect(url_for('task_status'))
    else:
        return render_template('task_selection.html')

@app.route('/task_status', methods=['GET'])
def task_status():
    task_status = te.get_task_status()
    return render_template('task_status.html', task_status=task_status)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_data = request.form
    fs.submit_feedback(feedback_data)
    return redirect(url_for('task_selection'))

if __name__ == '__main__':
    dm.setup_database()
    app.run(debug=True)
```