from flask import render_template
from app import main_app


@main_app.errorhandler(Exception)
def handle_error(e):
    return render_template("exception_page.html")
