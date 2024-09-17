import os
from itertools import cycle

def encrypt(text, key):
    result = bytearray()
    for c, k in zip(text, cycle(key)):
        result.append(ord(c) ^ k)
    return result

def main():
    flag = open("flag.txt", "r")
    key = os.urandom(7)
    encrypted_flag = encrypt(flag.read(), key)
    hex_result = ''.join(f'\\x{byte:02x}' for byte in encrypted_flag)
    print("Encrypted Flag: ",hex_result)

if __name__ == "__main__":
    main()
