from Crypto.Util.number import *
from random import getrandbits


def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits


flag = bytes_to_long("flag{this_is_a_fake_flag}".encode())
length = flag.bit_length()
print(flag)
print(length)

key = getrandbits(length)
cipher = flag ^ key

for i in range(32):
    key = ROL(key, pow(cipher, 3, length))
    cipher ^= key

for i in range(32):
    cipher ^= key
    key = ROL(key, length - pow(cipher, 3, length))

m = cipher ^ key
flag = long_to_bytes(m).decode()
if flag.startswith('flag'):
        print(long_to_bytes(m).decode())