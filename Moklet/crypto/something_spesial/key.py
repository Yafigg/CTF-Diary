# Teks yang diketahui
known_plaintext = "MOKLET{"

# Ciphertext yang terkait dari flag yang dienkripsi (dalam bentuk heksadesimal)
hex_ciphertext = "66beb7ecabf8b4"
ciphertext = bytearray.fromhex(hex_ciphertext)

# Menentukan kunci
key = bytearray()
for p, c in zip(known_plaintext, ciphertext):
    key.append(ord(p) ^ c)

# Menampilkan kunci yang ditemukan
print("Key: ", key)
