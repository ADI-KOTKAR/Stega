import stepic
from PIL import Image
import time
import hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Secret Message and key
message = input("Enter your secret message: ")
key= "abracadabra"

# Cover Image and Compression
im = Image.open("test_images/sample_image.jpeg")
im.save("temp_images/temp_flip.jpeg",optimize=True,quality=60)
im = Image.open("temp_images/temp_flip.jpeg")

# Input Rotational Flip
angle = str(input("Enter flip: ")).upper()

# HMAC Digest
hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod="sha1")
message_digest1 = hmac1.hexdigest()

# Start Time
start = time.time()

# Set Flip
if angle == "LR":
    im1 = im.transpose(Image.FLIP_LEFT_RIGHT)
elif angle == "TB":
    im1 = im.transpose(Image.FLIP_TOP_BOTTOM)
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

# Original Orientation of Image
if angle == "LR":
    im2 = enc.transpose(Image.FLIP_LEFT_RIGHT)
elif angle == "TB":
    im2 = enc.transpose(Image.FLIP_TOP_BOTTOM)
else:
    im2 = enc 

# Encoded Image
im2.save(f"encoded_images/{message_digest1}.png")
print(f"Encoded image : {message_digest1}.png")

# End Time
end = time.time()
print(end-start)