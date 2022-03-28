import stepic
from PIL import Image
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

message = input("Enter your secret message: ")
im = Image.open("test_images/sample_image.jpeg")

im.save("temp_images/temp.png",optimize=True,quality=60)
im = Image.open("temp_images/temp.png")

angle = int(input("Enter angle: "))

start = time.time()

if angle == 90:
    im1 = im.transpose(Image.ROTATE_90)
elif angle == 180:
    im1 = im.transpose(Image.ROTATE_180)
elif angle == 270:
    im1 = im.transpose(Image.ROTATE_270)
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
time.sleep(5)

if angle == 90:
    im2 = enc.transpose(Image.ROTATE_270)
elif angle == 180:
    im2 = enc.transpose(Image.ROTATE_180)
elif angle == 270:
    im2 = enc.transpose(Image.ROTATE_90)
else:
    im2 = enc 

im2.save("encoded_images/encoded_rotate.png")
end = time.time()
print(end-start)