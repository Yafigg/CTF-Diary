# Description

"ada hacker yang mencoba mengirimi sebuah pesan rahasia ke cyberspecters, dia ngirim
ke instagram cyberspecters, gmail cyberspecters, website cyberspecters, youtube
cyberspecters, linkedin cyberspecters. Sekarang bantu saya menerjemahkan bahasa
yang bikin saya bingung, kira kira ini bahasa apaa yaa? apakah bahasa alien? apa
bahasa robot? atau bahasa inggris? bahasa jerman? bahasa latin? bahasa rusia? bahasa
prancis? bahasa thailand? bahasa apaa yaa?"

# Solution

Disini kita diberi sebuah file .txt yang ketika saya buka isinya adalah
```
❯ cat Chall.txt
S1jJZL5MBnT7KYWLYT9EWVXBXH9WYcdSTF99
```
Dikarenakan deskripsi soalnya begini :

"ada hacker yang mencoba mengirimi sebuah pesan rahasia ke cyberspecters, dia ngirim ke instagram cyberspecters, gmail cyberspecters, website cyberspecters, youtube cyberspecters, linkedin cyberspecters. Sekarang bantu saya menerjemahkan bahasa yang bikin saya bingung, kira kira ini bahasa apaa yaa? apakah bahasa alien? apa bahasa robot? atau bahasa inggris? bahasa jerman? bahasa latin? bahasa rusia? bahasa prancis? bahasa thailand? bahasa apaa yaa?", kemungkinan teks tersebut bisa didecode menggunakan Vigenere Chiper, namun apa key nya ? saya memiliki list kemungkinan keynya

1. HACKER
2. CYBERSPECTERS
3. INSTAGRAM
4. GMAIL
5. WEBSITE
6. YOUTUBE
7. LINKEDID
8. ALIEN
9. ROBOT
10. INGGRIS
11. JERMAN
12. LATIN
13. RUSIA
14. PRANCIS
15. THAILAND

Dari ke 15 kemungkinan key diaatas mari kita ke Cyerchef untuk mencobanya.

Baru mencoba kemungkinan key yang kedua yaitu CYBERSPECTERS ternyata tembus namun harus kita decode kembali hasilnya ke Base64

S1jJZL5MBnT7KYWLYT9EWVXBXH9WYcdSTF99 = Vigenere Chiper : Key = CYBERSPECTERS
Q1lIVU5UMjR7RUFTWV9DSEFMTF9DUllQVE99 = Base64

# Summary

Vigenere Chiper : Key = CYBERSPECTERS > Base64 = Flag

CYHUNT24{EASY_CHALL_CRYPTO}

FLAG : CYHUNT24{EASY_CHALL_CRYPTO}

