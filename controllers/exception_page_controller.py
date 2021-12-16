from flask import render_template
from main import app


@app.errorhandler(Exception)
def handle_error(e):
    return render_template("exception_page.html")
