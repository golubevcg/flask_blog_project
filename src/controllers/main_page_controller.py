from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_migrate import Migrate
# from model.entity.db_data import db
from model.entity.user import User
from model.entity.post import Post


import os
import hashlib

from .post_page_controller import post_page_app
from .create_post_page_controller import create_page_app
from src.dao.post_dao import PostDao
from src.dao.user_dao import UserDao


app = Flask(__name__, template_folder='../../src/templates/html', static_folder='../../src/templates/static')

app.register_blueprint(post_page_app, url_prefix="/post")
app.register_blueprint(create_page_app, url_prefix="/create_new_post")

login_manager = LoginManager()
login_manager.login_view = 'login_get'
login_manager.init_app(app)

# db_login = os.environ["POSTGRESQL_LOGIN"]
# db_pwd = os.environ["POSTGRESQL_PWD"]
# db_port = "5432"
# db_name = "flask_blog"
# db_host = "localhost"

# app.config['SESSION_TYPE'] = 'filesystem'
# app.config["SESSION_TYPE"] = "filesystem"
# app.config["SESSION_FILE_DIR"] = "session"
# app.config["SESSION_USE_SIGNER"] = True
# app.config["SESSION_PERMANENT"] = True
app.secret_key = '9OLWxND4o83j4K4iuopO'
# app.config.update(SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{db_login}:{db_pwd}@{db_host}:{db_port}/{db_name}",
#                   SQLALCHEMY_TRACK_MODIFICATIONS=False,
#                   )
#
# db.init_app(app)
# app.config['SQLALCHEMY_ECHO'] = True
# migrate = Migrate(app, db)
# with app.app_context():
#     db.create_all()

post_dao = PostDao()
user_dao = UserDao()


@login_manager.user_loader
def load_user(user_id):
    user_dao = UserDao()
    # return user_dao.get_user_by_id(user_id)
    # from model.entity.user import User
    return user_dao.get_user_by_id(int(user_id))


@app.route("/")
def main():
    all_posts = post_dao.get_all_active_posts()
    all_posts = sorted(all_posts, key=lambda post: post.creation_date, reverse=True)
    posts_years = [post.creation_date.year for post in all_posts]
    temp_year = None
    for i in range(len(posts_years)):
        year = posts_years[i]
        if not temp_year:
            temp_year = year
            continue

        if year == temp_year:
            posts_years[i] = ""
        elif year != temp_year:
            temp_year = year

    return render_template("main_page.html", all_posts=all_posts, posts_years=posts_years)


@app.route("/about.html")
def about():
    return render_template("about_page.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/login", methods=['GET'])
def login_get():
    return render_template("login_page.html")


@app.route("/login", methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        flash('Please check your login details and try again.')
        return redirect(url_for('login_get'))

    password = str(password).encode()
    password = hashlib.md5(password).hexdigest()
    user = user_dao.get_user_by_login(login)
    if not user or user.password != password:
        flash('Please check your login details and try again.')
        return redirect(url_for('login_get'))
    else:
        login_user(user)
        return redirect("/")
