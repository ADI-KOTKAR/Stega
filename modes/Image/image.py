from flask import Blueprint, render_template

image = Blueprint("image", __name__, static_folder="static", template_folder="templates")

@image.route("/")
def image_home():
    return render_template("image.html")