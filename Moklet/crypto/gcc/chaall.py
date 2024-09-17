from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(256)
q = getPrime(256)
r = getPrime(256)

N1 = p*q
N2 = q*r

m = bytes_to_long(b"REDACTED")
e = 65537
c1 = pow(m, e, N1)
c2 = pow(m, e, N2)

print(f"{N1 = }")
print(f"{N2 = }")
print(f"{e = }")
print(f"{c1 = }")
print(f"{c2 = }")