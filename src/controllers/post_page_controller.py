from flask import Blueprint

post_page_app = Blueprint("post_page_app", __name__)


@post_page_app.route("/")
def main():
    return "post"


@post_page_app.route("/<int:post_id>")
def post_id(post_id="1"):
    return {"post": post_id}
