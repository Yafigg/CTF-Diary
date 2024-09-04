ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

ciphertext_bytes = bytes.fromhex(ciphertext_hex)

refined_key = b"myXORkey"

decrypted_flag = bytes([ciphertext_bytes[i] ^ refined_key[i % len(refined_key)] for i in range(len(ciphertext_bytes))])

flag = decrypted_flag.decode()

print("Flag :", flag)
