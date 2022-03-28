import stepic
from PIL import Image
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

im = Image.open("encoded_images/encoded_rotate.png")

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

key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'

cipherString = stepic.decode(im1)
cipherBytes = bytes(cipherString[2:-1], encoding='utf-8')
cipherBytes = cipherBytes.decode('unicode_escape').encode('latin1')
cipher2 = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher2.decrypt(cipherBytes), 16)
print("Decode text:",pt.decode())

end = time.time()
print(end-start)