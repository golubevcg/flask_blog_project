from flask import Blueprint, render_template, request
from flask_login import login_required

from src.services.logger_service import main_logger
from src.model.entity.post import Post
from src.dao import post_dao

create_new_post_blueprint = Blueprint(
                          "create_new_post_app", __name__,
                          template_folder='../templates/html',
                          static_folder='../templates/static'
                          )


@create_new_post_blueprint.route("/", methods=['GET'])
@login_required
def main():
    # redirect to main
    return render_template("/create_post_page.html")


@create_new_post_blueprint.route("/check_new_post_header_unique", methods=['POST'])
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


@create_new_post_blueprint.route("/save_new_post", methods=['POST'])
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