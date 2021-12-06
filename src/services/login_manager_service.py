from flask_login import LoginManager
from src.dao import user_dao

login_manager = LoginManager()
login_manager.login_view = 'login_get'


@login_manager.user_loader
def load_user(user_id):
    return user_dao.get_user_by_id(int(user_id))
