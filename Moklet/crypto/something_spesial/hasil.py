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

# Kunci yang ditemukan
key = bytearray(b'+\xf1\xfc\xa0\xee\xac\xcf')

# Mendekripsi seluruh ciphertext menggunakan kunci yang ditemukan
decrypted = bytearray()
for c, k in zip(ciphertext, cycle(key)):
    decrypted.append(c ^ k)

# Menampilkan hasil dekripsi
print("Decrypted Flag: ", decrypted.decode())
