from Crypto.Util.number import bytes_to_long, long_to_bytes
import string

png = "89 50 4E 47 0D 0A 1A 0A"
png_long = bytes_to_long(bytes.fromhex(''.join(png.split()))[:5])

chip = eval(open('enc', 'r').read())

key = chip[0] ^ png_long
print("Key :", key)

png = b""
for i in chip:
    decrypted = long_to_bytes(i ^ key).rjust(5, b'\0')
    png += decrypted

open('solved.png', 'wb').write(png)
