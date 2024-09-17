key_hex_spaced = "2b f1 fc a0 ee ac cf"
string_bytes = b"\x66\xbe\xb7\xec\xab\xf8\xb4\x78\x81\xcf\xc3\xdf\x98\xa3\x74\xc1\x8e\xff\xa0\x9c\xbb\x56"

# Pisahkan nilai hexadecimal yang dipisahkan dengan spasi
key_hex_list = key_hex_spaced.split()

# Konversi setiap nilai hexadecimal ke byte
key_bytes = b''
for hex_value in key_hex_list:
    key_bytes += bytes.fromhex(hex_value)

# Panjang key yang digunakan
key_length = len(key_bytes)

# Lakukan operasi XOR byte demi byte
result = bytearray()
for i, byte in enumerate(string_bytes):
    key_byte = key_bytes[i % key_length]  # Ambil key byte sesuai dengan index modulo panjang key
    result.append(byte ^ key_byte)       # Operasi XOR antara byte dari string dengan key byte

# Konversi hasil XOR ke dalam string ASCII
result_ascii = result.decode('ascii', errors='ignore')

print(result_ascii)
