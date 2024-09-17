flag_enc = [0x39, 0x2a, 0x27, 0x27, 0x2a, 0x39, 0x4a, 0x26, 0x56, 0x1a, 0x58, 0x1d, 0x58, 0x02, 0x2b, 0x55, 0x3e, 0x34, 0x2c, 0x1f, 0x48, 0x24, 0x11, 0x5c, 0x54, 0x12]
key = "telkom1"

# Converting key to ASCII values
key_ascii = [ord(c) for c in key]
key_len = len(key_ascii)

# Manual decryption
decrypted_chars = []
for i in range(len(flag_enc)):
    decrypted_char = chr(flag_enc[i] ^ key_ascii[i % key_len])
    decrypted_chars.append(decrypted_char)

# Joining the characters to form the decrypted flag
decrypted_flag = ''.join(decrypted_chars)
print("Decrypted flag:", decrypted_flag)
