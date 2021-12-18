import os

from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from services.db_service import db
from controllers.create_post_page_controller import create_new_post_blueprint
from controllers.post_page_controller import post_page_blueprint
from controllers.main_page_controller import main_page_blueprint
from services.login_manager_service import login_manager


app = Flask(__name__)
app.register_blueprint(main_page_blueprint, url_prefix="/")
app.register_blueprint(post_page_blueprint, url_prefix="/post")
app.register_blueprint(create_new_post_blueprint, url_prefix="/create_new_post")

CONFIG_OBJ = "config.%s" % os.getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(CONFIG_OBJ)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

login_manager.init_app(app)
csrf = CSRFProtect(app)

if __name__ == '__main__':
    app.run(debug=True, host=app.config["HOST"], port=app.config["PORT"])
