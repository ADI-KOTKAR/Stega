from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'Unaligned'   # 9 bytes
key = get_random_bytes(32)
iv = get_random_bytes(16)

cipher1 = AES.new(key, AES.MODE_CBC, iv)
ct = cipher1.encrypt(pad(data, 16))
print(ct)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher2.decrypt(ct), 16)
print(pt)
assert(data == pt)