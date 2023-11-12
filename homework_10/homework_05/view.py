from flask import Blueprint, render_template

index_app = Blueprint(
    "index_app",
    __name__,
    url_prefix="/"
)

@index_app.get("/", endpoint = "index")
def index_view():
    return render_template("index.html")

@index_app.get("/about/", endpoint = "about")
def about_view():
    return render_template("about.html")