from itertools import cycle

# Fungsi enkripsi yang disediakan
def encrypt(text, key):
    result = bytearray()
    for c, k in zip(text, cycle(key)):
        result.append(ord(c) ^ k)
    return result

# Ciphertext dari flag terenkripsi yang diberikan
hex_ciphertext = "66beb7ecabf8b47881cfc3df98a374c18effa09cbb56"
ciphertext = bytearray.fromhex(hex_ciphertext)

# Teks yang diketahui
known_plaintext = "MOKLET{"

# Menentukan kunci
key = bytearray()
for p, c in zip(known_plaintext, ciphertext):
    key.append(ord(p) ^ c)

# Mengubah kunci ke bentuk ASCII
key_ascii = ''.join(chr(k) for k in key)

# Mendekripsi seluruh ciphertext menggunakan kunci yang ditemukan
decrypted = bytearray()
for c, k in zip(ciphertext, cycle(key)):
    decrypted.append(c ^ k)

# Menampilkan kunci dan hasil dekripsi
print("Key (ASCII):", key_ascii)
print("Decrypted Flag:", decrypted.decode())
