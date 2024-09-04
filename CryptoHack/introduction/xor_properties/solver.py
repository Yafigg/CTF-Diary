from Crypto.Util.number import long_to_bytes

key1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_xor_key1_hex = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_xor_key3_hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_xor_keys_hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1 = bytes.fromhex(key1_hex)
key2_xor_key1 = bytes.fromhex(key2_xor_key1_hex)
key2_xor_key3 = bytes.fromhex(key2_xor_key3_hex)
flag_xor_keys = bytes.fromhex(flag_xor_keys_hex)

key2 = bytes([b1 ^ b2 for b1, b2 in zip(key2_xor_key1, key1)])

key3 = bytes([b1 ^ b2 for b1, b2 in zip(key2_xor_key3, key2)])

flag = bytes([b1 ^ b2 for b1, b2 in zip(flag_xor_keys, key1)])
flag = bytes([b1 ^ b2 for b1, b2 in zip(flag, key3)])
flag = bytes([b1 ^ b2 for b1, b2 in zip(flag, key2)])

print(flag.decode('ascii'))
