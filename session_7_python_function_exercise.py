# ===============================================================================================
# Soal 1
# Fungsi untuk mengubah angka menjadi label "Ganjil" atau "Genap"
def cek_ganjil_genap(angka):
    return "Genap" if angka % 2 == 0 else "Ganjil"

# Daftar list yang akan diproses
list1 = [1, 3, 4, 5]
list2 = [22, 17, 19, 20, 14]
list3 = [1, 3, 5]
list4 = [2, 4, 6]

# Menggunakan map untuk mengubah setiap elemen dalam list sesuai fungsi cek_ganjil_genap
hasil1 = list(map(cek_ganjil_genap, list1))
hasil2 = list(map(cek_ganjil_genap, list2))
hasil3 = list(map(cek_ganjil_genap, list3))
hasil4 = list(map(cek_ganjil_genap, list4))

# Menampilkan hasil
print("Hasil list1:", hasil1)  # Output: ['Ganjil', 'Ganjil', 'Genap', 'Ganjil']
print("Hasil list2:", hasil2)  # Output: ['Genap', 'Ganjil', 'Ganjil', 'Genap', 'Genap']
print("Hasil list3:", hasil3)  # Output: ['Ganjil', 'Ganjil', 'Ganjil']
print("Hasil list4:", hasil4)  # Output: ['Genap', 'Genap', 'Genap']

# ===============================================================================================
# Soal 2

# List harga yang akan difilter
harga = [9100000, 9800000, 9500000, 10300000, 9300000]

# Fungsi untuk memeriksa apakah harga lebih dari 9.300.000
def lebih_dari_9300000(x):
    return x > 9300000

# Menggunakan filter untuk mendapatkan harga yang lebih dari 9.300.000
hasil_filter = filter(lebih_dari_9300000, harga)
print("Harga lebih dari 9.300.000:", list(hasil_filter))  # Output: [9800000, 9500000, 10300000]

# Alternatif menggunakan lambda function
hasil_filter_lambda = filter(lambda x: x > 9300000, harga)
print("Harga lebih dari 9.300.000 (dengan lambda):", list(hasil_filter_lambda))  # Output: [9800000, 9500000, 10300000]

# ===============================================================================================
# Soal 3

# ===============================================================================================
