import hashlib
import math

from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user

from services.logger_service import main_logger
from dao import post_dao, user_dao


main_page_blueprint = Blueprint(
                                 "main_page_blueprint", __name__,
                                 template_folder='../templates/html',
                                 static_folder='../templates/static'
                                )


@main_page_blueprint.route("/")
@main_page_blueprint.route("/<page>")
def main(page=1):

    is_authenticated = current_user.is_authenticated

    if type(page) != int:
        try:
            page = int(page)
        except Exception as e:
            main_logger.warning(e)
            return

    if is_authenticated:
        all_posts = post_dao.get_all_posts_from_page(page)
    else:
        all_posts = post_dao.get_all_published_posts_from_page(page)

    posts_years = [post.creation_date.year for post in all_posts]
    temp_year = None
    for i in range(len(posts_years)):
        year = posts_years[i]
        if not temp_year:
            temp_year = year
            continue

        if year == temp_year:
            posts_years[i] = ""
        elif year != temp_year:
            temp_year = year

    posts_amount = post_dao.get_posts_amount()
    pages_amount = math.ceil(posts_amount / 10 )

    return render_template("main_page.html",
                           all_posts=all_posts,
                           posts_years=posts_years,
                           pages_amount=pages_amount,
                           page_num=page)


@main_page_blueprint.route("/about.html")
def about():
    return render_template("about_page.html")


@main_page_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@main_page_blueprint.route("/login", methods=['GET'])
def login_get():
    return render_template("login_page.html")


@main_page_blueprint.route("/login", methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        flash('Please check your login details and try again.')
        return render_template("login_page.html")

    password = str(password).encode()
    password = hashlib.md5(password).hexdigest()
    user = user_dao.get_user_by_login(login)
    if not user or user.password != password:
        flash('Please check your login details and try again.')
        return render_template("login_page.html")
    else:
        login_user(user)
        return redirect("/")
