```python
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from src.database_manager import UserSchema

login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data['id']
        self.username = user_data['username']
        self.password = user_data['password']

@login_manager.user_loader
def load_user(user_id):
    user_data = UserSchema.query.get(int(user_id))
    if user_data:
        return User(user_data)
    return None

def authenticate_user(username, password):
    user_data = UserSchema.query.filter_by(username=username).first()
    if user_data and user_data.password == password:
        user = User(user_data)
        login_user(user)
        return True
    return False

@login_required
def logout():
    logout_user()
```