def generate_valid_redeem_code():
    code = ['K', '3', 'M', 'O', 'E', '3', '3', 'c', 'T', '{', '4', 'T', 'd', 'h', '_', 'D', 'R', '0', 'L', '_', '}']
    swaps = [
        (0, 2), (3, 1), (18, 12), (20, 1), (11, 5), (6, 9), (10, 15),
        (16, 7), (18, 8), (6, 10), (14, 5), (6, 19), (18, 1), (20, 18)
    ]

    # Perform the swaps in reverse order to get the original code
    for swap in reversed(swaps):
        code[swap[0]], code[swap[1]] = code[swap[1]], code[swap[0]]

    return ''.join(code)

# Generate and print the valid redeem code
valid_redeem_code = generate_valid_redeem_code()
print(f"Valid redeem code: {valid_redeem_code}")
