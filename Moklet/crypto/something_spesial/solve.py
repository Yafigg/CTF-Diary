import os

encrypted_text = b'\x66\xbe\xb7\xec\xab\xf8\xb4\x78\x81\xcf\xc3\xdf\x98\xa3\x74\xc1\x8e\xff\xa0\x9c\xbb\x56'
prefix = b'MOKLET{'

def decrypt_with_key(encrypted_text, key):
    decrypted = bytearray()
    key_length = len(key)
    for i in range(len(encrypted_text)):
        decrypted.append(encrypted_text[i] ^ key[i % key_length])
    return decrypted

def brute_force_decrypt(encrypted_text, prefix, key_length, max_attempts):
    for attempt in range(max_attempts):
        key = os.urandom(key_length)
        decrypted = decrypt_with_key(encrypted_text, key)
        if decrypted.startswith(prefix):
            return decrypted.decode('utf-8', errors='ignore')
        if attempt % 1000000 == 0:
            print(f"Tried {attempt} keys...")
    return None

# Tentukan panjang kunci (dalam byte)
key_length = 7
# Batasan maksimum percobaan
max_attempts = 1000000000

result = brute_force_decrypt(encrypted_text, prefix, key_length, max_attempts)
if result:
    print(f"Plaintext found: {result}")
else:
    print("Plaintext not found within the given number of attempts.")
