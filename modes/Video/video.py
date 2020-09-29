from flask import Blueprint, render_template

video = Blueprint("video", __name__, static_folder="static", template_folder="templates")

@video.route("/")
def video_home():
    return render_template("video.html")