import ast
import random
import unicodedata

blacklist = [
    'exec', 'eval', 'str', 'compile', 'open', 'read', 'file', 'import', 'globals', 'locals', 'class', 'os', 'subprocess', 'input', 'setattr', 'getoutput', 'getattr', 'delattr', 'vars', '__', 'dir', 'builtin', 'base', 'help'
]

def Moklet():
    print("Selamat datang di Moklet Got Talent")
    print("Masukkan Penyanyi favoritmu:")

    inputt = input("> ")
    normalisasi = unicodedata.normalize('NFKD', inputt).encode('ASCII', 'ignore').decode()
    if any(func in normalisasi for func in blacklist):
        print("Keluar.")
        return

    Nama = eval(f"""\'{inputt}\'""") # Nama = ast.literal_eval(f"""\'{user_input}\'""")

    Awal = [
        f"Dalam sinar bulan, {Nama} menari anggun,",
        f"Di taman mimpi, {Nama} berbisik lembut,",
        f"Di antara bintang, {Nama} bersinar terang,",
        f"Setiap matahari terbit, {Nama} melukis langit dengan warna ilahi,"
    ]
    Tengah = [
        "Menginspirasi hati dan pikiran,",
        "Memikat semua yang melihat,",
        "Mempesona dengan setiap langkah,",
        "Membawa kebahagiaan ke dunia,"
    ]
    Akhir = [
        "Seorang muse yang tiada banding.",
        "Dalam setiap bait, sebuah kisah untuk dibagikan.",
        "Kecantikan abadi yang tiada tanding.",
        "Dalam setiap hati, selamanya ada."
    ]


    # Randomly selecting elements for the poem
    beginning = random.choice(Awal)
    middle = random.choice(Tengah)
    end = random.choice(Akhir)

    print(f"\n{beginning}\n{middle}\n{end}")

Moklet()

