"""Exercise Module 1 Day 4"""
# Soal 1a
# Bentuk 1 (dengan while loop)
# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

print (f"*** Bentuk 1 dengan while loop ***")
print (f"*** Pola Segitiga Menurun ***")

size = 5 # ukuran pola
i = size

while i > 0:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print() # Pindah baris baru
    i -= 1

print (f"*** Pola Segitiga Menaik ***")
i = 2
while i <= size:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print() # pindah baris baru
    i += 1

#=============================================================================================
print (f"*** Bentuk 1 dengan for loop ***")
print (f"*** Pola Segitiga Menurun ***")
# Soal 1b
# Bentuk 1 (dengan foor loop)
# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

size = 5 # ukuran maxs bintang di baris pertama

for i in range(size, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print() # Pindah ke baris baru

print (f"*** Pola Segitiga Menaik ***")
for i in range(2, size +1):
    for j in range(i):
        print("*", end=" ")
    print() # Pindah ke baris baru
#=============================================================================================
print (f"*** Bentuk 2 dengan while loop ***")
print (f"*** Pola Berlian ***")
# Soal 2a
# Bentuk 2 (dengan while loop)
# Tentukan Pola atas seperti Berlian
size = 5 # ukurang separuh bola

# Bagian pertama : Segitiga atas
i = 1
while i <= size:
    # Mencetak spasi untuk setiap baris
    j = 1
    while j <= size - i:
        print(" ", end=" ")
        j += 1
    # Mencetak bintang untuk setiap baris
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    print() # pindah barus baru
    i +=1

# Bagian kedua : Segitiga bawah
i = size - 1
while i > 0:
    # Cetak spasi untuk setiap baris
    j = 1
    while j <= size - i:
        print(" ", end=" ")
        j += 1
    # Cetak bintang untuk setiap baris
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    print()
    i -= 1
#=============================================================================================
print (f"*** Bentuk 2 dengan for loop ***")
print (f"*** Pola Berlian ***")
# Soal 2b
# Bentuk 2 (dengan foor loop)
size = 5

# Bagian pertama (atas)
for i in range(size):
    # Cetak spasi sebelum bintang
    for j in range(size - i - 1):
        print(" ", end=" ")
    # Cetak bintang
    for j in range(2 * i + 1):
        print("*", end=" ")
    print() # pindah baris baru

# Bagian kedua (bawah)
for i in range(size - 2, -1, -1):
    # Cetak spasi sebelum bintang
    for j in range(size - i -1):
        print(" ", end=" ")
    # Cetak bintang
    for j in range(2 * i +1):
        print("*", end=" ")
    print() # pindah baris baru

#======================================================================================================
print (f"*** Soal 2 - Belanja ***")
print (f"*** Belanja Buah ***")

# Variabel stok dan harga per buah
stok_buah = {
    "apel": 10,
    "jeruk": 7,
    "anggur": 6
}

harga_buah = {
    "apel": 10000,
    "jeruk": 15000,
    "anggur": 20000
}

# input jumlah buah dan memastikan tidak melebihi stok
def input_jumlah_buah(nama_buah):
    while True:
        jumlah = int(input(f"Masukkan jumlah {nama_buah}: "))
        if jumlah <= stok_buah[nama_buah]:
            return jumlah
        else:
            print(f"Jumlah yang dimasukkan terlalu banyak. Stok {nama_buah} hanya {stok_buah[nama_buah]}.")

# input jumlah buah
jumlah_apel = input_jumlah_buah("apel")
jumlah_jeruk = input_jumlah_buah("jeruk")
jumlah_anggur = input_jumlah_buah("anggur")

# Menghitung total harga setiap buah dan total belanja
total_apel = jumlah_apel * harga_buah["apel"]
total_jeruk = jumlah_jeruk * harga_buah["jeruk"]
total_anggur = jumlah_anggur * harga_buah["anggur"]
total_belanja = total_apel + total_jeruk + total_anggur

# Menampilkan detail belanja
print("\nDetail Belanja")
print(f"Apel : {jumlah_apel} x {harga_buah['apel']} = {total_apel}")
print(f"Jeruk : {jumlah_jeruk} x {harga_buah['jeruk']} = {total_jeruk}")
print(f"Anggur : {jumlah_anggur} x {harga_buah['anggur']} = {total_anggur}")
print(f"Total : {total_belanja}")

# Fungsi untuk meminta input jumlah uang dan memastikan cukup
def input_jumlah_uang(total):
    while True:
        jumlah_uang = int(input("Masukkan jumlah uang: "))
        if jumlah_uang < total:
            kekurangan = total - jumlah_uang
            print(f"Uang yang dimasukkan kurang sebesar {kekurangan}. Silakan masukkan jumlah uang yang cukup.")
        else:
            return jumlah_uang

# Meminta input jumlah uang dari user
jumlah_uang = input_jumlah_uang(total_belanja)

# Menampilkan hasil pembayaran
if jumlah_uang == total_belanja:
    print("Terima kasih")
elif jumlah_uang > total_belanja:
    kembalian = jumlah_uang - total_belanja
    print("Terima kasih")
    print(f"Uang kembali anda: {kembalian}")
