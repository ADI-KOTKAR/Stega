import os
from flask import Blueprint, current_app, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename

image = Blueprint("image", __name__, static_folder="static", template_folder="templates")

@image.route("/encode")
def image_encode():
    return render_template("encode-image.html")

@image.route("/encode-result", methods = ['POST', 'GET'])
def image_encode_result():
    if request.method == 'POST':
      if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
      file = request.files['image']
      if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
      if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_IMAGE_FOLDER'], filename))
      result = request.form
      return render_template("encode-result.html", result = result, file=file)

@image.route("/decode")
def image_decode():
    return render_template("decode-image.html")