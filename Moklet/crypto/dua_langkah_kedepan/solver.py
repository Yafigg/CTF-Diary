def decrypt_caesar(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                decrypted_char = chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                decrypted_char = chr((shifted - ord('A')) % 26 + ord('A'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Read ciphertext from file
with open('chall.txt', 'r') as f:
    ciphertext = f.read().strip()

# Define shift based on the key 'xktij'
shift = [23, 10, 19, 8, 9]

# Decrypt ciphertext using the shifts
plaintext = decrypt_caesar(ciphertext, shift[0])

# Wrap the plaintext in the requested format
flag_format = "MOKLET{{{}}}".format(plaintext)

print(flag_format)
