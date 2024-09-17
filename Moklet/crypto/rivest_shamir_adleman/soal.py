from Crypto.Util.number import *

FLAG=b'REDACTED'
e=0x10001

p,q=[getStrongPrime(1024) for _ in range(2)]
n=p*q

pt=bytes_to_long(FLAG)
ct=pow(pt,e,n)

leak = p+(p**2+p*q+p)*(q**2+p*q+q)

print('leak       : ',leak)
print('n          : ',n)
print('e          : ',e)
print('ciphertext : ',ct)
