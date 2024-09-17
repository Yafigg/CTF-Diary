dasar dasar RSA

1. **`n`** - the public modulus obtained by applying a formula to a pair of **large** prime numbers **`p`** and **`q`**
2. **`e`** - the public encryption exponent used to encrypt a plaintext message **`m`**
3. **`c`** - the encrypted message i.e the cipher text / file.enc
4. **`d`** - the decryption exponent computed by applying a function over **`p`**, **`q`** and **`n`**.
5. **`m`** - message / pesan 

So now encryption using RSA can be mathematically expressed as:

> c = m$^e$ mod(n)  
> where **`mod`** is the modulus operator

and decryption from RSA can be expressed as:

> m = c$^d$ mod(n)  
> where again **`mod`** is the modulus operator

Now take a look at the encryption formula, and think what happens when the value of me is smaller than the value of **`n`** or **`n`** is very large than the exponent **`e`**.

Well you guessed it right, **`c`** i.e the cipher text would be equal to me and the effect of encryption reduces to merely raising the plaintext message to the power of the exponent **`e`**.

Given the above background read ahead.

## C , N dan E

contoh

```bash
c = 10400286653072418349777706076384847966640064725838262071
n = 23519325203263800569051788832344215043304346715918641803
e = 71
```

```bash
./RsaCtfTool.py -n <N> -e <E> --uncipher <C>
```

dicari nilai p dan q dari factordb.com dari nilai n

contoh source nya

```python
from Crypto.Util.number import inverse, long_to_bytes 

c = <nilai c>
n = <nilai n>
e = <nilai e> 
p = <nilai p> 
q = <nilai q> 

phi = (p-1)*(q-1) 
d = inverse(e, phi) 
m = pow(c,d,n) 
print(long_to_bytes(m))
```


apabila N nilainya sangat besar dan E sangat kecil
misal

```bash
e: 3
c: 2780321436921227845269766067805604547641764672251687438825498122989499386967784164108893743279610287605669769995594639683212592165536863280639528420328182048065518360606262307313806591343147104009274770408926901136562839153074067955850912830877064811031354484452546219065027914838811744269912371819665118277221
n: 23571113171923293137414347535961677173798389971011031071091131271311371391491511571631671731791811911931971992112232272292332392412512572632692712772812832933073113133173313373473493533593673733793833893974014094194214314334394434494574614634674794874914995035095215235415475575635695715775875935996016076136176196316416436476536596616736776836917017097197277337397437517577617697737877978098118218238278298398538578598638778818838879079119199299379419479539679719779839919971009101310191431936117404941729571877755575331917062752829306305198341421305376800954281557410379953262534149212590443063350628712530148541217933209759909975139820841212346188350112608680453894647472456216566674289561525527394398888860917887112180144144965154878409149321280697460295807024856510864232914981820173542223592901476958693572703687098161888680486757805443187028074386001621827485207065876653623459779938558845775617779542038109532989486603799040658192890612331485359615639748042902366550066934348195272617921683
```

```bash
$pip install pycryptodome
$pip install sympy
```

```python
from Crypto.Util.number import long_to_bytes
from sympy import cbrt
m=cbrt(<C>)
print(long_to_bytes(m))
```

## P,Q dan E


```python
from Crypto.Util.number import inverse
#--------Data--------#
p = <p>
q = <q>
e = <e>
#--------RSA--------#
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(d)
```


## P,Q,E dan C

```bash
/RsaCtfTool.py -p <p> -q <q> -e <e> --uncipher <c>
```

## public key(pub.key) dan chipertext

1. dicari private key dengan RsaCtfTool bruteforce 

```bash
./RsaCtfTool.py --publickey ./pub.key --private
```

2. dicari flag

```bash
$openssl rsautl -in flag.enc -out flag.txt -decrypt -inkey priv.key
```



## public key

mendapatkan n, e dari public key

```bash
./RsaCtfTool.py --publickey pub.key --dumpkey
```

mendapatkan n, e, d, p, q

```bash
./RsaCtfTool.py --publickey pub.key --dumpkey --private
```


## Rabin cryptosystem

```python
#!/usr/bin/env python3
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB

#--------Data--------#

with open("pubkey.pem","r") as f1, open("flag.enc", "rb") as f2:
    key = RSA.import_key(f1.read())
    N = key.n
    e = key.e
    c = bytes_to_long(f2.read())
    print(f"{N = }")
    print(f"{e = }")
    print(f"{c = }")

#--------FactorDB--------#

f = FactorDB(N)
f.connect()
factors = f.get_factor_list()

p = factors[0]
q = factors[1]

#--------Rabin Cryptosystem--------#

inv_p = inverse(p, q)
inv_q = inverse(q, p)

m_p = pow(c, (p + 1) // 4, p)
m_q = pow(c, (q + 1) // 4, q)

a = (inv_p * p * m_q + inv_q * q * m_p) % N
b = N - int(a)
c = (inv_p * p * m_q - inv_q * q * m_p) % N
d = N - int(c)

plaintext_list = [a, b, c, d]

for plaintext in plaintext_list:
    s = str(hex(plaintext))[2:]

    # padding with 0
    if len(s) % 2 != 0:
        s = "0" + s
    print(bytes.fromhex(s))
```


## coprime e2

soal 
```python
#!/usr/bin/env python

import random

N = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929L

def pad_even(x):
    return ('', '0')[len(x)%2] + x

e1 = 17
e2 = 65537


fi = open('flag.txt','rb')
fo1 = open('flag.enc1','wb')
fo2 = open('flag.enc2','wb')


data = fi.read()
fi.close()

while (len(data)<512-11):
    data  =  chr(random.randint(0,255))+data

data_num = int(data.encode('hex'),16)

encrypt1 = pow(data_num,e1,N)
encrypt2 = pow(data_num,e2,N)


fo1.write(pad_even(format(encrypt1,'x')).decode('hex'))
fo2.write(pad_even(format(encrypt2,'x')).decode('hex'))

fo1.close()
fo2.close()
```

contoh

```python
#!/usr/bin/env python3
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA
from sympy import gcdex
from sys import exit

#--------Data--------#

N = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929
e1 = 17
e2 = 65537

with open("flag.enc1","rb") as f1, open("flag.enc2", "rb") as f2:
    c1 = bytes_to_long(f1.read())
    c2 = bytes_to_long(f2.read())
    print(f"{c1 = }")
    print(f"{c2 = }")

#--------Common Modulus--------#

r, s, gcd = gcdex(e1, e2)
r = int(r)
s = int(s)

# Test if e1 and e2 are coprime
if gcd != 1:
    print("e1 and e2 must be coprime")
    exit()

m = (pow(c1, r, N) * pow(c2, s, N)) % N
flag = long_to_bytes(m)

print(flag)
```


## Multi prime RSA

solusi
cari faktor prima dari factordb.com tulis di primes

```python

#python2

n = 396024192066637812510450621382035407862868088296947670690301497371475295939904796980243233322894266141620734205143095605424207925368340802690646297450491
c = 94601003975036014892627558903765140006414154753639040877983052130842889430185826661689965123628679020897585326580781804995645118941447092101126138087372
e = 65537

#ambil faktor prima dari n dari factordb.com
primes = [ 2520734081,2963163041,2968229111,3010828267,3170708137,3256290119,3356156009,3368813909,3468273229,3671092039,3679173373,3760110227,4012932073,4076280259,4135959361,4264770803]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

ts = []
xs = []
ds = []

for i in range(len(primes)):
    ds.append(modinv(e, primes[i]-1))

m = primes[0]

for i in range(1, len(primes)):
    ts.append(modinv(m, primes[i]))
    m = m * primes[i]

for i in range(len(primes)):
    xs.append(pow((c%primes[i]), ds[i], primes[i]))

x = xs[0]
m = primes[0]

for i in range(1, len(primes)):
    x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
    m = m * primes[i]

print hex(x%n)[2:-1].decode("hex")
```