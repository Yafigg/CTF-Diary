from Crypto.Util.number import bytes_to_long
import secrets

def encrypt(x, y):
    with open(x, 'rb') as f:
        flag = f.read()
    key = secrets.randbits(64)
    chunks = [flag[i:i+5] for i in range(0, len(flag), 5)]
    flag_long = [bytes_to_long(chunk) for chunk in chunks]

    encrypt = [chunk ^ key for chunk in flag_long]
    with open(y, 'w') as enc_file:
        enc_file.write(str(encrypt))

if __name__ == '__main__':
    encrypt('flag.png', 'enc')
