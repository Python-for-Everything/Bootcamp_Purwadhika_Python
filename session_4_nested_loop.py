# Soal 1
# Memulai dari angka 9 sampai 1
angka = int(input("Masukkan Angka : "))

# Looping untuk 3 baris
for i in range(3):
    for j in range(3):
        print(angka, end=" ")
        angka -= 1
    print()
print()
#============================================
# Soal 2
print()
list_angka = [1,2,3,4,5,6,7,8,9,10]
for i in list_angka:
    if i % 3 == 0:
        pass
    else:
        print(i ** 2, end= " ")
print()
#============================================
# Soal 3
print()
# Menentukan jumlah baris awal
jumlah_baris = 5

# Loop pola bintang menurun
for i in range(jumlah_baris, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()
#============================================
# Soal 4
# print (f"*** Pola Segitiga Menurun ***")

size = 5
i = size

while i > 0:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print() #
    i -= 1

#print (f"*** Pola Segitiga Menaik ***")
i = 2
while i <= size:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
print()
#============================================
# Soal 5
# Inisialisasi stok dan harga per buah
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

# Fungsi untuk meminta input jumlah buah dan memastikan tidak melebihi stok
def input_jumlah_buah(nama_buah):
    while True:
        jumlah = int(input(f"Masukkan jumlah {nama_buah}: "))
        if jumlah <= stok_buah[nama_buah]:
            return jumlah
        else:
            print(f"Jumlah yang dimasukkan terlalu banyak. Stok {nama_buah} hanya {stok_buah[nama_buah]}.")

# Meminta input jumlah buah
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
