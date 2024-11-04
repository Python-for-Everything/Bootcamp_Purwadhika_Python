# =============================================================================================
# Python Filter Function
# List awal
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fungsi untuk mengecek apakah sebuah angka genap
def is_genap(x):
    return x % 2 == 0

# Menggunakan filter dengan fungsi is_genap
hasil_genap = filter(is_genap, angka)
print(list(hasil_genap))  # Output: [2, 4, 6, 8, 10]

# Menggunakan filter dengan lambda function untuk hasil yang sama
hasil_genap_lambda = filter(lambda x: x % 2 == 0, angka)
print(list(hasil_genap_lambda))  # Output: [2, 4, 6, 8, 10]

# =============================================================================================
# Python Filter Function
# Contoh 1: Memfilter Angka Ganjil
# List angka
angka = [1, 2, 3, 4, 5]

# Fungsi untuk memeriksa apakah sebuah angka ganjil
def is_ganjil(x):
    return x % 2 != 0

# Menggunakan filter untuk memfilter angka ganjil
angka_ganjil = filter(is_ganjil, angka)
print("Angka ganjil:", list(angka_ganjil))  # Output: [1, 3, 5]
# =============================================================================================
# Python Filter Function
# Contoh 2: Memfilter Harga yang Lebih dari 9.000.000
# List harga
harga = [9100000, 9800000, 9500000, 10300000, 9300000]

# Fungsi untuk memeriksa apakah harga lebih dari 9.000.000
def lebih_dari_sembilan_juta(x):
    return x > 9000000

# Menggunakan filter untuk memfilter harga yang lebih dari 9.000.000
harga_tinggi = filter(lebih_dari_sembilan_juta, harga)
print("Harga lebih dari 9.000.000:", list(harga_tinggi))  # Output: [9800000, 9500000, 10300000]

# =============================================================================================
# Python Filter Function
# List angka yang akan difilter
list1 = [1, 2, 3, 4, 5]

# Fungsi untuk memeriksa apakah sebuah angka adalah genap
def angkaGenap(angka):
    return angka % 2 == 0

# Menggunakan filter dengan fungsi angkaGenap
hasilFilter = filter(angkaGenap, list1)
print(hasilFilter, type(hasilFilter))  # Menampilkan objek filter dan tipe datanya

# Mengonversi objek filter menjadi list
hasilFilterList = list(hasilFilter)
print(hasilFilterList)  # Output: [2, 4]

# Menggunakan filter dengan lambda function untuk hasil yang sama
hasilFilterList1 = list(filter(lambda angka: angka % 2 == 0, list1))
print(hasilFilterList1)  # Output: [2, 4]

# =============================================================================================
# Python Filter Function
# Definisi fungsi filterDuplikat untuk memfilter elemen dalam collection
def filterDuplikat(fn, collection):
    # Membuat list baru untuk menyimpan hasil
    newCollection = []
    # Memeriksa setiap item dalam collection dengan kondisi dari fn
    for item in collection:
        if fn(item):  # Jika kondisi True, item ditambahkan ke newCollection
            newCollection.append(item)
    # Mengembalikan list baru yang hanya berisi elemen yang memenuhi kondisi
    return newCollection

# List angka yang akan difilter
list1 = [1, 2, 3, 4, 5]

# Definisi fungsi angkaGenap untuk memeriksa angka genap
def angkaGenap(angka):
    return angka % 2 == 0

# Menggunakan filterDuplikat dengan fungsi angkaGenap
newList = filterDuplikat(angkaGenap, list1)
print(newList)  # Output: [2, 4]

# Menggunakan filterDuplikat dengan lambda function untuk hasil yang sama
print(filterDuplikat(lambda angka: angka % 2 == 0, list1))
# Output: [2, 4]

# =============================================================================================
#
