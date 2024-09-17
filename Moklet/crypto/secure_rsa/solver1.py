from Crypto.Util.number import bytes_to_long, long_to_bytes

# Given values
n = 1048576
e = 65537
enc = 475005

# Function to calculate modular inverse
def mod_inverse(e, phi):
    d = pow(e, -1, phi)
    return d

# Find prime factors of n
p = 1024  # Since n = 1024 * 1024 = 1048576
q = 1024

# Calculate phi(n)
phi_n = (p - 1) * (q - 1)

# Calculate private exponent d
d = mod_inverse(e, phi_n)

# Decrypt the ciphertext
decrypted = pow(enc, d, n)

# Convert the decrypted number back to bytes and print as a string
plaintext = long_to_bytes(decrypted).decode('latin-1')
print("Decrypted message:", plaintext)
