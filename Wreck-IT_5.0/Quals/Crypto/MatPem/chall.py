import random

FLAG = b"WRECKIT50{????????}"
fint = int(FLAG.hex(),16)
key = [random.getrandbits(4) for _ in range(3)]

pk = [
   [11,14,17,20], [12,15,18,21], [13,16,19,22]
]

result = [sum([key[j]*pk[i][j] for j in range(3)]) for i in range(3)]

var = ['a','b','c','d']
for i in range(len(pk)):
    equation = ''
    for j in range(len(pk[i])):
        equation += str(pk[i][j])+"*"+var[j]+" + "
    equation = equation[:-3] + " = " + str(result[i])
    print(equation)

key = sum(key)

enc = key*fint
print("Encryted flag:", enc)


"""
Output:
11*a + 14*b + 17*c + 20*d = 263
12*a + 15*b + 18*c + 21*d = 282
13*a + 16*b + 19*c + 22*d = 301
Encryted flag: 232248373780702558559732705634320310324639111824357224567527709756665492238132012558072443413580231257415
"""
