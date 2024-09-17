# Encrypted flag in hex
encrypted_flag_hex = "\x66\xbe\xb7\xec\xab\xf8\xb4\x78\x81\xcf\xc3\xdf\x98\xa3\x74\xc1\x8e\xff\xa0\x9c\xbb\x56"

# Convert the hex string to bytes
encrypted_flag = bytes.fromhex(encrypted_flag_hex.replace('\\x', ''))

# Key "MOKLET{"
key = "MOKLET{"
key_bytes = key.encode()

# Decrypt the flag by XORing each byte
decrypted_flag = bytearray()
for i in range(len(encrypted_flag)):
    decrypted_flag.append(encrypted_flag[i] ^ key_bytes[i % len(key_bytes)])

# Convert the decrypted bytes to a string
decrypted_flag_str = decrypted_flag.decode()

print(decrypted_flag_str)
