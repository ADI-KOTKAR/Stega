from flask import Blueprint, render_template

text = Blueprint("text", __name__, static_folder="static", template_folder="templates")

@text.route("/")
def text_home():
    return render_template("text.html")