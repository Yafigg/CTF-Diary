# Description

bantu saya cari steg steg donkk puhh sepuhhh saya pusing, aman aja
puh nggak dukun inii cuman butuh effort ajaaaaaaaaaa.

# Solution

Di soal steg kali ini kita lagi-lagi diberikan file gambar yang berformat .jpeg, seperti biasaa kita lihat
metadatanya terlebih dahulu

```❯ exiftool chall.jpeg
ExifTool Version Number : 12.76
File Name : chall.jpeg
Directory : .
File Size : 12 kB
File Modification Date/Time : 2024:05:31 23:43:25+07:00
File Access Date/Time : 2024:06:01 09:38:20+07:00
File Inode Change Date/Time : 2024:06:01 09:38:13+07:00
File Permissions : -rw-r--r--
File Type : JPEG
File Type Extension : jpg
MIME Type : image/jpeg
JFIF Version : 1.01
Resolution Unit : None
X Resolution : 1
Y Resolution : 1
Image Width : 266
Image Height : 190
Encoding Process : Baseline DCT, Huffman coding
Bits Per Sample : 8
Color Components : 3
Y Cb Cr Sub Sampling : YCbCr4:2:0 (2 2)
Image Size : 266x190
Megapixels : 0.051
❯ file chall.jpeg
chall.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16,
baseline, precision 8, 266x190, components 3
❯ binwalk chall.jpeg
DECIMAL HEXADECIMAL DESCRIPTION
--------------------------------------------------------------------------------
0 0x0 JPEG image data, JFIF standard 1.01
```
Tidak ada yang mencurigakan, karena nama soalnya steg saya curiga ini menggunakan tools steg
seperti steghide atau yang lainnya, karena saya tidak mempunyai steghide dan adanya stegseek jadi
mari kita coba saja.

```❯ stegseek chall.jpeg ~/Assets/wordlist/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "cyber")           
[i] Original filename: "flag.txt".
[i] Extracting to "chall.jpeg.out".

❯ cat chall.jpeg.out
CYHUNT24{masih_easy-lahh_yaaa}
```

# Flag = CYHUNT24{masih_easy-lahh_yaaa}
