from flask import Blueprint, redirect, render_template
from src.dao.post_dao import PostDao

login_page_app = Blueprint("login_page_app", __name__,
                          template_folder='../../src/templates/html',
                          static_folder='../../src/templates/static'
                          )


@login_page_app.route("/")
def login():
    # redirect to main
    return render_template("login_page.html")

