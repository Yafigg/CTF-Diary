import string

hex_string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

encoded_bytes = bytes.fromhex(hex_string)

def xor_single_byte(byte_data, key):
    return bytes([b ^ key for b in byte_data])

for key in range(256):
    decoded_bytes = xor_single_byte(encoded_bytes, key)
    try:
        decoded_string = decoded_bytes.decode('ascii')
        if all(c in string.printable for c in decoded_string):
            print(f"Key: {key}, Decoded String: {decoded_string}")
    except UnicodeDecodeError:
        continue
