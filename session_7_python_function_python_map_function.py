# ==============================================================================================
# Python Map and Filter Function

# map(cbFunction, collections)

# Fungsi untuk mengalikan sebuah angka dengan 2
def kali_dua(x):
    return x * 2

# List angka
angka = [1, 2, 3, 4, 5]

# Menggunakan map untuk menerapkan kali_dua ke setiap item di angka
hasil = list(map(kali_dua, angka))

print("Hasil map:", hasil)
# ==============================================================================================
# Python Map Function
# List angka asli
angka = [1, 2, 3, 4, 5]

# Menggunakan map untuk mengalikan setiap elemen dengan 2
hasil_kali_dua = list(map(lambda x: x * 2, angka))

print("Hasil kali dua:", hasil_kali_dua)

# ==============================================================================================
# 1. Syntax Lambda Function
# Lambda function untuk menambahkan dua angka
tambah = lambda x, y: x + y

# Memanggil lambda function
hasil = tambah(5, 3)
print("Hasil penjumlahan:", hasil)

# 2. Lambda Function di Dalam Map
# List angka
angka = [1, 2, 3, 4]

# Menggunakan map dengan lambda function untuk mengalikan setiap elemen dengan 2
hasil = list(map(lambda x: x * 2, angka))

print("Hasil map dengan lambda:", hasil)

# 3. Lambda Function di Dalam filter
# List angka
angka = [1, 2, 3, 4, 5, 6]

# Menggunakan filter dengan lambda function untuk memilih angka genap
hasil = list(filter(lambda x: x % 2 == 0, angka))

print("Hasil filter dengan lambda:", hasil)

# ==============================================================================================
# Lambda Examples

# 1. Lambda Function untuk Mengalikan dengan 2
# Lambda function untuk mengalikan angka dengan 2
kali2 = lambda angka: angka * 2

# Memanggil lambda function dengan input 7
print(kali2(7))  # Output: 14

# ==============================================================================================
# 2. Lambda Function untuk Penjumlahan Dua Angka
# Lambda function untuk menjumlahkan dua angka
tambah = lambda angka1, angka2: angka1 + angka2

# Memanggil lambda function dengan input 15 dan 2
print(tambah(15, 2))  # Output: 17

# 3. Lambda Function untuk Pengurangan Tiga Angka
# Lambda function untuk mengurangi tiga angka
kurang = lambda angka1, angka2, angka3: angka1 - angka2 - angka3

# Memanggil lambda function dengan input 20, 4, dan 6
print(kurang(20, 4, 6))  # Output: 10

# ==============================================================================================
# Python Map Function
# List awal
list1 = [1, 2, 3, 4, 5]

# Fungsi untuk mengalikan sebuah angka dengan 2
def kali2(angka):
    return angka * 2

# Menggunakan fungsi map dengan fungsi kali2
hasilMap = map(kali2, list1)
print(hasilMap, type(hasilMap))  # Menampilkan objek map dan tipe datanya


# Mengonversi objek map menjadi list
hasilMapList = list(hasilMap)
print(hasilMapList)  # Output: [2, 4, 6, 8, 10]

# Menggunakan map dengan lambda function
hasilMapList1 = list(map(lambda angka: angka * 2, list1))
print(hasilMapList1)  # Output: [2, 4, 6, 8, 10]

# ==============================================================================================
# Python Map Function
# Definisi fungsi mapDuplikat untuk memproses elemen dalam collection
def mapDuplikat(fn, collection):
    # Membuat list baru untuk menyimpan hasil
    newCollection = []
    # Memproses setiap item dalam collection dengan fungsi fn
    for item in collection:
        newCollection.append(fn(item))
    # Mengembalikan list baru yang sudah diproses
    return newCollection

# List yang akan diproses
list1 = [1, 2, 3, 4, 5]

# Definisi fungsi ubah untuk memformat angka
def ubah(angka):
    return 'Angka {}'.format(angka)

# Menggunakan mapDuplikat dengan fungsi ubah dan list1
newList = mapDuplikat(ubah, list1)
print(newList)  # Output: ['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']

# Menggunakan mapDuplikat dengan lambda function untuk hasil yang sama
print(mapDuplikat(lambda angka: 'Angka {}'.format(angka), list1))
# Output: ['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']

# ==============================================================================================
#