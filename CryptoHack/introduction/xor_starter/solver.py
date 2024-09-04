label = "label"

xor_value = 13

new_string = ''.join(chr(ord(char) ^ xor_value) for char in label)

print(f"crypto{{{new_string}}}")
