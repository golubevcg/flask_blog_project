from flask import Flask, render_template
from .post_page_controller import post_page_app
from src.dao.post_dao import PostDao


app = Flask(__name__, template_folder='../../src/templates/html', static_folder='../../src/templates/static')
app.register_blueprint(post_page_app, url_prefix="/post")


@app.route("/")
def main():
    post_dao = PostDao()
    all_posts = post_dao.get_all_active_posts()
    return render_template("main_page.html")


# @app.route("/hello/")
# @app.route("/hello/<username>/")
# def hello_user(username="World"):
#     return f"Hello {username}!!"



