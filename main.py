import os

from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from services.db_service import db
from controllers.create_post_page_controller import create_new_post_blueprint
from controllers.post_page_controller import post_page_blueprint
from controllers.main_page_controller import main_page_blueprint
from services.login_manager_service import login_manager

app = Flask(__name__, template_folder='templates/html', static_folder='templates/static')
app.register_blueprint(main_page_blueprint, url_prefix="/")
app.register_blueprint(post_page_blueprint, url_prefix="/post")
app.register_blueprint(create_new_post_blueprint, url_prefix="/create_new_post")

# db_login = 'postgres'
# db_pwd = '123'
# db_port = "5432"
# db_name = "flask_blog"
# db_host = "localhost"

# main_app.config["SESSION_TYPE"] = "filesystem"
# main_app.config["SESSION_FILE_DIR"] = "session"
# main_app.config["SESSION_USE_SIGNER"] = True
# main_app.config["SESSION_PERMANENT"] = True
# main_app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
# main_app.config.update(
#                       SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{db_login}:{db_pwd}@{db_host}:{db_port}/{db_name}",
#                       SQLALCHEMY_TRACK_MODIFICATIONS=False,
#                       )

CONFIG_OBJ = "config.%s" % os.getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(CONFIG_OBJ)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

login_manager.init_app(app)
csrf = CSRFProtect(app)

app.run(debug=True, host=app.config["HOST"], port=app.config["PORT"])