from stegano import lsb
from os.path import isfile, join

import time  # install time ,opencv,numpy modules
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import run, call, STDOUT
from flask import Blueprint, render_template, current_app, url_for, redirect, request, session, flash
from datetime import timedelta
# from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename

video = Blueprint("video", __name__, static_folder="static",
                  template_folder="templates")


@video.route("/encode")
def video_encode():

    return render_template("encode-video.html")


@video.route("/encode-result", methods=['POST', 'GET'])
def video_encode_result():
    if request.method == 'POST':
        message = request.form['message']
        if 'file' not in request.files:
            flash('No video found')
            # return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('No selected video')
            # return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                current_app.config['UPLOAD_VIDEO_FOLDER'], filename))
            encryption = True
            encrypt(os.path.join(
                current_app.config['UPLOAD_VIDEO_FOLDER'], filename), message)
        else:
            encryption = False
        result = request.form
        return render_template("encode-video-result.html", message=message, result=result, file=file, encryption=encryption)


@video.route("/decode")
def video_decode():
    return render_template("decode-video.html")


@video.route("/decode-result", methods=['POST', 'GET'])
def video_decode_result():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No Video found')
            # return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('No selected video')
            # return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                current_app.config['UPLOAD_VIDEO_FOLDER'], filename))
            decryption = True
            decrpytedText = decrypt(os.path.join(
                current_app.config['UPLOAD_VIDEO_FOLDER'], filename))
        else:
            decryption = False
        result = request.form
        return render_template("decode-video-result.html", result=result, decrypytedText=decrpytedText, file=file, decryption=decryption)


# encrypt Video

def encrypt(f_name, input_string):
    frame_extraction(f_name)
    print(os.getcwd())
    path = str(os.getcwd()) + \
        "\modes\Video\\ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg"
    print(path)
    # command = path + " -i "+ f_name + " -q:a 0 -map a" + str(os.getcwd())+"/tmp/audio.mp3 -y"
    # os.system(command)
    # run([path, "-i", f_name, "-q:a", "0", "-map", "a",
    #      str(os.getcwd())+"/tmp/audio.mp3", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

    encode_string(input_string)
    sec_command = path + " -i tmp/%d.png -vcodec png modes/Video/static/enc-video.mp4 -y"
    print(sec_command)
    os.system(sec_command)
    # call([path, "-i", "tmp/%d.png", "-vcodec", "png", "video.mov",
    #       "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

    # third_command = path + ""
    # call([path, "-i", "video.mov", "-i", "tmp/audio.mp3", "-codec",
    #       "copy", "data/enc-" + str(f_name)+".mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)


def split_string(s_str, count=10):
    per_c = math.ceil(len(s_str)/count)
    c_cout = 0
    out_str = ''
    split_list = []
    for s in s_str:
        out_str += s
        c_cout += 1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str = ''
            c_cout = 0
    if c_cout != 0:
        split_list.append(out_str)
    return split_list


def frame_extraction(video):
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    temp_folder = "./tmp"
    print("[INFO] tmp directory is created")

    vidcap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1


def encode_string(input_string, root="./tmp/"):
    split_string_list = split_string(input_string)
    for i in range(0, len(split_string_list)):
        f_name = "{}{}.png".format(root, i)
        secret_enc = lsb.hide(f_name, split_string_list[i])
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name, split_string_list[i]))


def decrypt(video):
    frame_extraction(video)
    secret = []
    root = "./tmp/"
    for i in range(len(os.listdir(root))):
        f_name = "{}{}.png".format(root, i)
        secret_dec = lsb.reveal(f_name)
        if secret_dec == None:
            break
        secret.append(secret_dec)
    result = ''.join([i for i in secret])
    print(result)
    clean_tmp()
    return result


def clean_tmp(path="./tmp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] tmp files are cleaned up")
