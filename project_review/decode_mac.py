import stepic
from PIL import Image
import time
import hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Input Encoded Image
img_name = input(str("Enter encoded image name: "))
im = Image.open(f"encoded_images/{img_name}.png")

# Input Rotational Angle
angle = int(input("Enter angle: "))

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

# AES Decryption for Secret Message
key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'

cipherString = stepic.decode(im1)
cipherBytes = bytes(cipherString[2:-1], encoding='utf-8')
cipherBytes = cipherBytes.decode('unicode_escape').encode('latin1')
cipher2 = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher2.decrypt(cipherBytes), 16)
print("Decoded text:",pt.decode())

# HMAC Verification
key = "abracadabra"
hmac2 = hmac.new(key=key.encode(), digestmod="sha1")
hmac2.update(bytes(pt.decode(), encoding="utf-8"))
message_digest2 = hmac2.hexdigest()

if img_name==message_digest2:
    print('The signature is authentic.')
else:
    print('The signature is not authentic.')

# End Time
end = time.time()
print(end-start)