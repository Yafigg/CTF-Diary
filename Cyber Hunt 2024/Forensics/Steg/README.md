# Description

Diberikan sebuah file gambar 

# Solution

Untuk mendapatkan flagnya bisa menggunakan stegseek sesuai dengan judulnya :

```❯ stegseek chall.jpeg ~/Assets/wordlist/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "cyber")           
[i] Original filename: "flag.txt".
[i] Extracting to "chall.jpeg.out".

❯ cat chall.jpeg.out
CYHUNT24{masih_easy-lahh_yaaa}


## Flag: CYHUNT24{masih_easy-lahh_yaaa} 
