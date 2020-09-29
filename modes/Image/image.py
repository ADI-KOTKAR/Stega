from flask import Blueprint, render_template

image = Blueprint("image", __name__, static_folder="static", template_folder="templates")

@image.route("/encode")
def image_encode():
    return render_template("encode-image.html")

@image.route("/decode")
def image_decode():
    return render_template("decode-image.html")