# Konversi m menjadi ASCII
m = 8141666172599015327517844412077350450662655857598898032249398714749

# Konversi m menjadi bytes
m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')

# Decode bytes menjadi string
plaintext = m_bytes.decode()
print(plaintext)
