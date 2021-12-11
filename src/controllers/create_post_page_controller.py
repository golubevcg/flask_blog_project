import json

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
def create_post_page():
    # redirect to main
    return render_template("/create_post_page.html")


@create_new_post_blueprint.route("/<post_id>", methods=['GET'])
@login_required
def edit_existing_post_page(post_id: int):

    if not post_id:
        return

    try:
        post_id = int(post_id)
    except Exception as e:
        main_logger.exception(e)

    post = post_dao.get_post_by_id(post_id)
    if not post:
        main_logger.exception(f"Edit post error, cannot find post with this id:{str(id)}")
        return

    return render_template("/create_post_page.html", post=post)


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


@create_new_post_blueprint.route("/check_post_with_this_id_exists", methods=['POST'])
@login_required
def check_post_id_is_valid():
    post_id = request.get_json(silent=True)
    if not post_id:
        return ""
    post_id = int(post_id)

    post = post_dao.get_post_by_id(post_id)
    if post:
        return "valid post"
    else:
        return ""


@create_new_post_blueprint.route("/save_new_post", methods=['POST'])
def save_post():
    post_data = request.get_json(silent=True)
    if "header" not in post_data:
        return ""

    if "body" not in post_data:
        return ""

    header = post_data["header"]
    header_length = len(header)
    if header_length < 5 or header_length > 50:
        main_logger.exception("Header length does not fit between 5 and 50 symbols, saving interrupted!")
        return ""

    body = post_data["body"]
    is_published = post_data["is_published"]
    is_link_access = post_data["is_link_access"]
    is_deleted = post_data["is_deleted"]

    post = None
    if "post_id" in post_data:
        post_id = post_data["post_id"]
        post = post_dao.get_post_by_id(post_id)
        if not post:
            main_logger.exception(f"Cannot update post with such id, "
                                  f"because no post with this id was founded. "
                                  f"(post_id = {str(post_id)}")
            return ""

    json_string = json.dumps(body)

    try:
        if post:
            if post.header != header and post_dao.get_post_with_by_header(header):
                return

            post.header = header
            post.body = json_string
            post.is_published = is_published
            post.is_link_access = is_link_access
            post.is_deleted = is_deleted
            post_dao.commit()
        else:
            if post_dao.get_post_with_by_header(header):
               return

            post = Post(
                        header,
                        json_string,
                        is_published=is_published,
                        is_link_access=is_link_access,
                        is_deleted=is_deleted
                        )
            post_dao.save_post(post)
        return "Post added successfully"
    except Exception as e:
        main_logger.exception(e)
        return ""