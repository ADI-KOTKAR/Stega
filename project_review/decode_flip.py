import stepic
from PIL import Image
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

im = Image.open("encoded_images/encoded_rotate.png")

angle = str(input("Enter flip: ")).upper()

start = time.time()

if angle == "LR":
    im1 = im.transpose(Image.FLIP_LEFT_RIGHT)
elif angle == "TB":
    im1 = im.transpose(Image.FLIP_TOP_BOTTOM)
else:
    im1 = im

key = b'mysecretpasswordmysecretpassword'
iv = b'mysecretpassword'

cipherString = stepic.decode(im1)
print(cipherString)
cipherBytes = bytes(cipherString[2:-1], encoding='utf-8')
cipherBytes = cipherBytes.decode('unicode_escape').encode('latin1')
cipher2 = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher2.decrypt(cipherBytes), 16)
print("Decode text:",pt.decode())

end = time.time()
print(end-start)