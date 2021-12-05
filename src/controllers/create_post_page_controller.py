from flask import (
    Blueprint,
    redirect,
    render_template,
    url_for,
    request,
    jsonify,
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
)

from src.services.logger_service import main_logger
from src.model.entity.post import Post
from src.dao.post_dao import PostDao
import json


create_page_app = Blueprint("create_page_app", __name__,
                          template_folder='../../src/templates/html',
                          static_folder='../../src/templates/static'
                          )

post_dao = PostDao()


@create_page_app.route("/", methods=['GET'])
@login_required
def main():
    # redirect to main
    return render_template("/create_post_page.html")


@create_page_app.route("/check_new_post_header_unique", methods=['POST'])
@login_required
def check_new_post_header_unique():
    header = request.get_json(silent=True)
    if not header:
        return ""

    posts = post_dao.get_post_with_by_header(header)
    if posts:
        return ""
    else:
        return "valid header"


@create_page_app.route("/save_new_post", methods=['POST'])
def save_post():
    post_data = request.get_json(silent=True)
    if "header" not in post_data:
        return ""

    if "body" not in post_data:
        return ""

    header = post_data["header"]
    body = post_data["body"]

    try:
        post = Post(header, body)
        post_dao.save_post(post)
        return "Post added successfully"
    except Exception as e:
        main_logger.log(e)
        return ""