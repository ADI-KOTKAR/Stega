from flask import Blueprint, render_template

video = Blueprint("video", __name__, static_folder="static", template_folder="templates")

@video.route("/encode")
def video_encode():
    return render_template("encode-video.html")

@video.route("/decode")
def video_decode():
    return render_template("decode-video.html")