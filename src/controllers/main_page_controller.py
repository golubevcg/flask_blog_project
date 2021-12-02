from flask import Flask, render_template
from .post_page_controller import post_page_app
from src.dao.post_dao import PostDao


app = Flask(__name__, template_folder='../../src/templates/html', static_folder='../../src/templates/static')
app.register_blueprint(post_page_app, url_prefix="/post")


@app.route("/")
def main():
    post_dao = PostDao()
    all_posts = post_dao.get_all_active_posts()
    all_posts = sorted(all_posts, key=lambda post: post.creation_date, reverse=True)
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

    return render_template("main_page.html", all_posts=all_posts, posts_years=posts_years)


@app.route("/about.html")
def about():
    print("I'm here!")
    return render_template("about_page.html")



