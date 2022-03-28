from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b'hello world'

ciphertext= cipher.encrypt(pad(plaintext, AES.block_size))

# print(ciphertext)
# print(cipher.iv)

with open('cipher_file', 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)