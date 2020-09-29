from flask import Blueprint, render_template

audio = Blueprint("audio", __name__, static_folder="static", template_folder="templates")

@audio.route("/")
def audio_home():
    return render_template("audio.html")