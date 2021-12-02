from flask import Blueprint, redirect, render_template
from src.dao.post_dao import PostDao

post_page_app = Blueprint("post_page_app", __name__,
                          template_folder='../../src/templates/html',
                          static_folder='../../src/templates/static'
                          )


@post_page_app.route("/")
def main():
    # redirect to main
    return redirect("/")


@post_page_app.route("/<post_id>")
def post_id(post_id=None):
    template_if_empty = render_template("post_page.html", header="This post was lost in space!", body="", creation_date="")
    if not post_id:
        return template_if_empty

    post_dao = PostDao()
    post = post_dao.get_post_by_id(int(post_id))

    if not post:
        return template_if_empty

    header = post.header
    body = post.body
    creation_date = post.creation_date.strftime("%d %b %Y")
    return render_template("post_page.html", header=header, body=body, creation_date=creation_date)

