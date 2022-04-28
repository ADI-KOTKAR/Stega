import stepic
from PIL import Image
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Input Encoded Image
img_name = input(str("Enter encoded image name: "))
im = Image.open(f"encoded_images/{img_name}.png")

# Input Rotational Angle
angle = int(input("Enter angle: "))

# Start Time
start = time.time()

# Digital Signature Verification
key = RSA.import_key(open('certificates/public_key.pem').read())
sig_msg = bytes(img_name, encoding='utf-8')

f = open('certificates/signature.pem', 'rb')
signature = f.read()
f.close()

hash2 = SHA256.new(sig_msg)

try:
    pkcs1_15.new(key).verify(hash2, signature)
    print('The signature is authentic.')
except (ValueError, TypeError):
    print('The signature is not authentic.')
    exit()

# Set Rotational Angle
if angle == 90:
    im1 = im.transpose(Image.ROTATE_90)
elif angle == 180:
    im1 = im.transpose(Image.ROTATE_180)
elif angle == 270:
    im1 = im.transpose(Image.ROTATE_270)
else:
    im1 = im

# AES Decryption for Secret Message
key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'

cipherString = stepic.decode(im1)
cipherBytes = bytes(cipherString[2:-1], encoding='utf-8')
cipherBytes = cipherBytes.decode('unicode_escape').encode('latin1')
cipher2 = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher2.decrypt(cipherBytes), 16)
print("Decode text:",pt.decode())

# End Time
end = time.time()
print(end-start)