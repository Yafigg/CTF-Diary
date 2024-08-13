from Crypto.Util.number import *
import random
from secret import enc_flag, prime_list

e = 65537
def RSA(pt):
    m = bytes_to_long(pt.encode())
    p,q = random.choice(prime), random.choice(prime)
    n = p*q
    c = pow(m,e,n)
    
    print(f'p = {p}')
    print(f'q = {q}')
    print(f'e = 65537')
    print(f'ciphertext = {c}\n')


def main():
    while True:
        print("1. Enkripsi")
        print("2. Ambil FLAG terenkripsi")
        print("3. Dekripsi")
        print("4. Keluar")
        
        choice = input("Pilih menu (1/2/3): ")

        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            encrypted = RSA(plaintext)

        elif choice == '2':
            print(enc_flag + "\n")
        
        elif choice == '3':
            print("dekripsi sendiri ya, hehe\n")

        elif choice == '4':
            print("Keluar")
            break

        else:
            print("Pilih yang ada aja ya")

if __name__ == "__main__":
    main()