hex_string = "\\x66\\xbe\\xb7\\xec\\xab\\xf8\\xb4\\x78\\x81\\xcf\\xc3\\xdf\\x98\\xa3\\x74\\xc1\\x8e\\xff\\xa0\\x9c\\xbb\\x56"

# Hilangkan karakter escape '\\' dan split berdasarkan '\\x'
hex_values = hex_string.replace("\\x", " ").split()

# Konversi setiap nilai heksadesimal menjadi byte
byte_data = bytearray.fromhex(''.join(hex_values))

# Hitung panjang teks asli dalam byte
length_of_text = len(byte_data)

print("Panjang teks asli (dalam byte):", length_of_text)
