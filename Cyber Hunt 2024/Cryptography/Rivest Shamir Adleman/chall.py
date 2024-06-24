from Crypto.Util.number import *
flag = bytes_to_long(b";HelloWorld(printf)")
p = getPrime(2048)
q = getPrime(2048)
r = getRandomInteger(20)
n = p*q
c = pow(flag,65537,n)
leak = (p-r)*(q-r)
print(f"""
{c = }
{n = }
{leak = }
""")
