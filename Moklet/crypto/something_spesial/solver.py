# Hasil enkripsi (dalam byte)
encrypted_bytes_long = b'\x66\xbe\xb7\xec\xab\xf8\xb4\x78\x81\xcf\xc3\xdf\x98\xa3\x74\xc1\x8e\xff\xa0\x9c\xbb\x56'

# Kunci XOR (7 byte)
key_7bytes = b'\x81\x8d\x7a\x9a\x22\x24\x14'

# Mengulang kunci sepanjang teks enkripsi
repeated_key = (key_7bytes * (len(encrypted_bytes_long) // len(key_7bytes) + 1))[:len(encrypted_bytes_long)]

# Melakukan XOR untuk setiap byte
decrypted_bytes_long = bytes([c ^ k for c, k in zip(encrypted_bytes_long, repeated_key)])

# Konversi hasil dekripsi ke string
decrypted_text_long = decrypted_bytes_long.decode(errors='ignore')

print("Hasil dekripsi:", decrypted_text_long)
print("Bytes hasil dekripsi:", decrypted_bytes_long)
