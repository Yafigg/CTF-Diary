def decrypt(enc_text, key):
    decrypted = []
    key_len = len(key)
    
    for i in range(len(enc_text)):
        decrypted_char = chr(ord(enc_text[i]) ^ ord(key[i % key_len]))
        decrypted.append(decrypted_char)
    
    return ''.join(decrypted)

flag_enc = "\x39\x2a\x27\x27\x2a\x39\x4a\x26\x56\x1a\x58\x1d\x58\x02\x2b\x55\x3e\x34\x2c\x1f\x48\x24\x11\x5c\x54\x12"
key = "telkom1"

decrypted_flag = decrypt(flag_enc, key)
print("Decrypted flag:", decrypted_flag)
