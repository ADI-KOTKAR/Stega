from flask import Blueprint, render_template

text = Blueprint("text", __name__, static_folder="static", template_folder="templates")

@text.route("/encode")
def text_encode():
    return render_template("encode-text.html")

@text.route("/decode")
def text_decode():
    return render_template("decode-text.html")