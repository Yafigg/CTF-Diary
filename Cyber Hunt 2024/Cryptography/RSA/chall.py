from Crypto.Util.number import bytes_to_long, getPrime, inverse

f = b"CYHUNT24{REDACTED}"
flag = bytes_to_long(f)

p = getPrime(2056)
q = getPrime(2056)

n = p * q
e = 65537
c = pow(flag, e, n)

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
dp = d * p
p2q = p**2 * q