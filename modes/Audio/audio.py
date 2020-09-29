from flask import Blueprint, render_template

audio = Blueprint("audio", __name__, static_folder="static", template_folder="templates")

@audio.route("/encode")
def audio_encode():
    return render_template("encode-audio.html")

@audio.route("/decode")
def audio_decode():
    return render_template("decode-audio.html")