# Teks yang diketahui dalam representasi byte
teks_diketahui = b"MOKLET{"

# Teks hasil XOR dalam heksadesimal
teks_xor_hex = bytes([0x66, 0xbe, 0xb7, 0xec, 0xab, 0xf8, 0xb4])

# Mencari kunci dengan melakukan XOR
kunci = bytearray(len(teks_diketahui))
for i in range(len(teks_diketahui)):
    kunci[i] = teks_diketahui[i] ^ teks_xor_hex[i]

# Hasil kunci dalam heksadesimal
kunci_hex = kunci.hex()

print(kunci_hex)
