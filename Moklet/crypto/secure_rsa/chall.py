from Crypto.Util.number import *
from secret import p, q, flag

n = p*q
e = 65537

def encrypt(n, secret):
    plaint = bytes_to_long(secret)
    chipper = pow(plaint, e, n)
    return chipper

def file(chipper):
    file = open("output.txt", "w")
    file.write("n = " + str(n))
    file.write("\ne = " + str(e))
    file.write("\nchipper = " + str(chipper))
    file.close

c = encrypt(n, flag)
file(c)
