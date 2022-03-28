from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'mysecretpassword'

with open('cipher_file', 'rb') as c_file:
    iv = c_file.read(16)
    ciphertext = c_file.read()

cipher = AES.new(key, AES.MODE_CBC)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(plaintext)
