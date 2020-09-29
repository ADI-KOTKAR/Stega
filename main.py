from flask import Flask, render_template
from Image.image import image
from Audio.audio import audio
from Text.text import text
from Video.video import video

app = Flask(__name__)
app.register_blueprint(image, url_prefix="/image")
app.register_blueprint(audio, url_prefix="/audio")
app.register_blueprint(text, url_prefix="/text")
app.register_blueprint(video, url_prefix="/video")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)