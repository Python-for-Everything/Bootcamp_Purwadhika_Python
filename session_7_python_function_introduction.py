# Contoh regular function untuk menjumlahkan dua angka:
# Definisi Regular Function
def tambah(angka1, angka2):
    # Fungsi ini menerima dua parameter, angka1 dan angka2
    # dan mengembalikan hasil penjumlahan keduanya
    return angka1 + angka2

# Pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil penjumlahan menggunakan regular function:", hasil)

# ==============================================================================================
# Contoh lambda function untuk menjumlahkan dua angka:
# Definisi Lambda Function
tambah_lambda = lambda angka1, angka2: angka1 + angka2

# Pemanggilan fungsi
hasil_lambda = tambah_lambda(3, 5)
print("Hasil penjumlahan menggunakan lambda function:", hasil_lambda)

# ==============================================================================================
#