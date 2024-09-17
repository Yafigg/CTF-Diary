from itertools import cycle

# Provided encryption function
def encrypt(text, key):
    result = bytearray()
    for c, k in zip(text, cycle(key)):
        result.append(ord(c) ^ k)
    return result

# Ciphertext from provided encrypted flag
hex_ciphertext = "66 be b7 ec ab f8 b4 78 81 cf c3 df 98 a3 74 c1 8e ff a0 9c bb 56"
ciphertext = bytearray.fromhex(hex_ciphertext)

# Known plaintext
known_plaintext = "MOKLET{"

# Determine the key from the known plaintext and corresponding ciphertext
key = bytearray()
for p, c in zip(known_plaintext, ciphertext):
    key.append(ord(p) ^ c)

# Decrypt the entire ciphertext using the determined key
decrypted = bytearray()
for c, k in zip(ciphertext, cycle(key)):
    decrypted.append(c ^ k)

# Print the decrypted result
print("Decrypted Flag: ", decrypted.decode())
