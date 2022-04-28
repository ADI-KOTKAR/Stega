import stepic
from PIL import Image
import time
import string
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Secret Message
message = input("Enter your secret message: ")

# Key generation - Public/Private Keys
key = RSA.generate(2048)

private_key = key.export_key()
f = open('certificates/private_key.pem', 'wb')
f.write(private_key)
f.close()

public_key = key.export_key()
f = open('certificates/public_key.pem', 'wb')
f.write(public_key)
f.close()

# Cover Image
im = Image.open("test_images/sample_image.jpeg")
im.save("temp_images/temp.png",optimize=True,quality=60)
im = Image.open("temp_images/temp.png")

# Input Rotational Angle
angle = int(input("Enter angle: "))

# Digital Signature
rndm_txt = ''.join(random.choices(string.ascii_uppercase+string.digits, k = 16))
img_name = bytes(rndm_txt, encoding='utf-8')

key = RSA.import_key(open('certificates/private_key.pem').read())
hash = SHA256.new(img_name)
signature = pkcs1_15.new(key).sign(hash)

f = open('certificates/signature.pem', 'wb')
f.write(signature)
f.close()

# Start Time
start = time.time()

# Set Rotational Angle
if angle == 90:
    im1 = im.transpose(Image.ROTATE_90)
elif angle == 180:
    im1 = im.transpose(Image.ROTATE_180)
elif angle == 270:
    im1 = im.transpose(Image.ROTATE_270)
else:
    im1 = im

# AES Encryption for Secret Message
key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'
cipher1 = AES.new(key, AES.MODE_CBC, iv)
ct = cipher1.encrypt(pad(bytes(message, encoding='utf-8'), 16))
print(ct)

# LSB Steganography
enc = stepic.encode(im1, bytes(str(ct), encoding='utf-8'))
enc.show()
time.sleep(5)

# Original Rottional Angle of Image
if angle == 90:
    im2 = enc.transpose(Image.ROTATE_270)
elif angle == 180:
    im2 = enc.transpose(Image.ROTATE_180)
elif angle == 270:
    im2 = enc.transpose(Image.ROTATE_90)
else:
    im2 = enc 

# Encoded Image
im2.save(f"encoded_images/{rndm_txt}.png")
print(f"Encoded image : {rndm_txt}.png")

# End Time
end = time.time()
print(end-start)