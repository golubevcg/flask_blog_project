from flask import Blueprint, redirect, render_template

from dao import post_dao
from flask_login import login_required
import random


post_page_blueprint = Blueprint(
                                "post_page_app", __name__,
                                template_folder='../templates/html',
                                static_folder='../templates/static'
                                )


@post_page_blueprint.route("/")
def main():
    # redirect to main
    return redirect("/")


@post_page_blueprint.route("/<post_header>")
def post_page(post_header=None):
    template_if_empty = render_template("post_page.html", header="This post was lost in space!", body="", creation_date="")
    if not post_header:
        return template_if_empty

    post_header = post_header.replace("_", " ")
    post = post_dao.get_post_with_header_like(post_header)

    if not post:
        return template_if_empty
    post = post[0]

    header = post.header
    body = post.body
    body = body.strip("\"")

    creation_date = post.creation_date.strftime("%d %b %Y")
    random_duck_index = random.randint(1, 4)

    return render_template(
        "post_page.html", 
        header=header, 
        body=body, 
        creation_date=creation_date,
        load_single_duck=True,
        random_duck_index=random_duck_index)


@post_page_blueprint.route("/delete_post/<int:post_id>", methods=['POST'])
@login_required
def delete_post(post_id):
    if not post_id:
        return ""
    post_dao.delete_post_by_id(post_id)
    return "Post successfully been deleted!"
