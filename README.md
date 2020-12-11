
<!-- PROJECT LOGO -->
<br />
<p align="center">
  
  <img src="https://img.icons8.com/color/80/000000/data-encryption.png"/>
  
  <h1 align="center">Stega</h1>

  <p align="center">
    A Steganography Tool
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://drive.google.com/file/d/1hOWJVv_HxIVPX7SOtW9EZjpMvlLsj5ix/view?usp=sharing">View Demo</a>
  </p>
</p>


<p align="center">
  <img src="https://github.com/ADI-KOTKAR/Stega/blob/master/images/home.PNG">
</p>

<!-- TABLE OF CONTENTS -->


## Table of Contents

* [About the Project](#about-the-project)
* [Resources](#resources)
* [Getting Started](#getting-started)
* [Contributors](#contributors)


<!-- ABOUT THE PROJECT -->
## About The Project

*Steganography* can also be referred as the technique of hiding secret data within an ordinary, non secret, file or message in order to avoid detection; the secret data is then extracted at its destination. 

**Stega** is a Python-Flask based Web App ehich serves the purpose of a Steganograhy tool which includes the functionality of following techniques in a single application:
- 📃 | 🖼️ Image Steganography
- 🎵 Audio Steganography 
- 📹 Video Steganography

## Resources
1. **Framework** : Flask
- [Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/)
2. **Image Steganography** : *opencv-python, stepic*
- [OpenCV documentation](https://docs.opencv.org/master/)
- [Stepic](https://pypi.org/project/stepic/)
2. **Audio Steganography** : *wave*
- [Wave Read & Write files](https://docs.python.org/3/library/wave.html)
2. **Video Steganography** : *stegano, subprocess, ffmpeg*
- [Stegano Documentation](https://stegano.readthedocs.io/)


<!-- GETTING STARTED -->
## Getting Started
#### Clone the Repo
```
git clone https://github.com/ADI-KOTKAR/Stega.git
````

####  Python 3 
Install Python 3 in your system. [click here](https://www.python.org/downloads/)

#### Create a Virtual Environment.
- Create a Virtual Environment using **Anaconda Navigator** with Python version 3.7+ 
- Open Terminal with the activated environment.

#### Installing Dependencies in Virtual Environment
- Make sure environment is activated. 
- Using Requirements File. **(Recommended)**
```
pip install -r requirements.txt
```
- Individually installing packages.
	##### ***Flask | OpenCv | Stepic | Wave | Stegano***
```
pip install Flask opencv-python stepic wave stegano
```
#### File Configuration
- Ensure that `static` folder is present inside each mode - Audio, Image, Text, Video inside `modes` directory. 
```
📦modes
 ┣ 📂Audio
 ┃ ┣ 📂static
 ┃ ┣ 📂templates
 ┃ ┣ 📜audio.py
 ┃ ┗ 📜__init__.py
 ┣ 📂Image
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📜sample.jpg
 ┃ ┣ 📂templates
 ┃ ┣ 📜image.py
 ┃ ┗ 📜__init__.py
 ┣ 📂Text
 ┃ ┣ 📂static
 ┃ ┣ 📂templates
 ┃ ┣ 📜text.py
 ┃ ┗ 📜__init__.py
 ┗ 📂Video
 ┃ ┣ 📂ffmpeg-4.3.1-2020-10-01-full_build
 ┃ ┣ 📂static
 ┃ ┣ 📂templates
 ┃ ┣ 📜video.py
 ┃ ┗ 📜__init__.py
```

If you have made it so far then you are genius enough to configure and build this application yourself. :clap: 

#### Running Application
Make sure environment is activated, Now run:
```
python main.py
```
Open the localhost link - [http://127.0.0.1:5000/](http://127.0.0.1:5000/),this will open the App on your browser.
You can use the sample files for testing in `test_files` folder.

## Contributors

- **Aditya Kotkar** - [ADI-KOTKAR](https://github.com/ADI-KOTKAR)
- **Shreyas Khadapkar** - [shreyaskhadapkar](https://github.com/shreyaskhadapkar)
- **Praveenkumar Khatri** - [PraveenKhatri](https://github.com/PraveenKhatri)

## License

- Project link: [Stega](https://github.com/ADI-KOTKAR/Stega)
- [License](https://github.com/ADI-KOTKAR/Stega/blob/master/LICENSE)


