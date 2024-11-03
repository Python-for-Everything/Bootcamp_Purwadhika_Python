# ====================================================================================================
# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 1 """
print(f"*** Tampilkan Huruf K ***")

# Kalimat
kalimat = "Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini"

# Pisahkan kalimat menjadi kata-kata
kata = kalimat.split()  # Splits the string at the specified separator, and returns a list

# Cari kata yang berawalan huruf 'k' atau 'K'
for kata in kata:
    if kata.lower().startswith('k'):  # Returns true if the string starts with the specified value
        print(kata)

print()
# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 2 """
print(f"*** Tampilkan Angka Yang Habis di Bagi 3 ***")

# Loop dari 1 - 50
for i in range(1, 51):
    # Cek jika angka habis dibagi 3
    if i % 3 == 0:
        print(i)
print()
# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 3 """
print(f"*** Tampilkan karaketer jumlah genap ***")

# Kalimat
kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'

# Pisah kalimat menjadi kata-kata
kata_kata = kalimat.split()  # Splits the string at the specified separator, and returns a list

# Cari dan Tampilkan kata yang memiliki jumlah karakter genap
for kata in kata_kata:
    if len(kata) % 2 == 0:
        print(kata)

# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 4 """
print(f"*** Tampilkan angka 1 - 100 dengan spesifik ***")
# Loop 1 - 100
for i in range(1, 101):
    # Cek jika kelipatan 3 dan 5
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} adalah kelipatan 3 & 5")
    # Cek jika kelipatan 3
    elif i % 3 == 0:
        print(f"{i} adalah kelipatan 3")
    # Cek jika kelipatan 5
    elif i % 5 == 0:
        print(f"{i} adalah kelipatan 5")
    # Bukan kelipatan 3 atau 5,
    else:
        print(i)
print()
# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 5 """
print(f"*** Cari Angka Tertinggi ***")

# List Angka
list_angka = [12, 15, 1, 7, 4, 100]

# Variabel angka tertinggi
angka_tertinggi = list_angka[0]

# Loop setiap angka dalam list
for angka in list_angka:
    if angka > angka_tertinggi:
        angka_tertinggi = angka

# Tampilkan angka tertinggi
print("Angka tertinggi di dalam list adalah:", angka_tertinggi)

# ====================================================================================================
""" Exercise Looping Statement"""
""" Soal 6 """
print(f"*** Buat Spesifik Output ***")

# Buat Baris
baris = int(input("Masukkan Jumlah Baris Maksimal : "))

# Buat Kolom
for i in range(1, baris + 1):
    for y in range(1, i + 1):
        print(y, end=" ")
    print()
# ====================================================================================================

