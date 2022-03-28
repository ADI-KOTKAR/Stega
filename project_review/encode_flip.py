import stepic
from PIL import Image
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
# import cv2

message = input("Enter your secret message: ")
im = Image.open("test_images/sample_image.jpeg")

im.save("temp_images/temp_flip.jpeg",optimize=True,quality=60)
im = Image.open("temp_images/temp_flip.jpeg")

angle = str(input("Enter flip: ")).upper()

start = time.time()

if angle == "LR":
    im1 = im.transpose(Image.FLIP_LEFT_RIGHT)
elif angle == "TB":
    im1 = im.transpose(Image.FLIP_TOP_BOTTOM)
else:
    im1 = im

# aes
key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'
cipher1 = AES.new(key, AES.MODE_CBC, iv)
ct = cipher1.encrypt(pad(bytes(message, encoding='utf-8'), 16))
print(ct)

enc = stepic.encode(im1, bytes(str(ct), encoding='utf-8'))
enc.show()
# time.sleep(5)

if angle == "LR":
    im2 = enc.transpose(Image.FLIP_LEFT_RIGHT)
elif angle == "TB":
    im2 = enc.transpose(Image.FLIP_TOP_BOTTOM)
else:
    im2 = enc 

im2.save("encoded_images/encoded_flip.png")
end = time.time()
print(end-start)
# print(stepic.decode(im2))