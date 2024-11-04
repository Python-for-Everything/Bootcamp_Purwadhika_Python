# ==============================================================================================
# Callback Function
# Definisi callback function (Function B)
def proses_data(data):
    print(f"Memproses data: {data}")

# Definisi fungsi utama yang menerima fungsi lain sebagai callback (Function A)
def eksekusi(callback, data):
    print("Eksekusi dimulai...")
    callback(data)  # Memanggil fungsi callback dengan argument data
    print("Eksekusi selesai.")

# Memanggil fungsi eksekusi dan meneruskan fungsi proses_data sebagai callback
eksekusi(proses_data, "Data Penjualan")

# ==============================================================================================
# Callback Function
#
# Fungsi penjumlahan
def tambah(num1, num2):
    return num1 + num2

# Fungsi pengurangan
def kurang(num1, num2):
    return num1 - num2

# Fungsi utama yang menerima fungsi lain sebagai callback
def hitung(fnOperator, angka1, angka2):
    hasil = fnOperator(angka1, angka2)  # Memanggil fungsi callback dengan argument angka1 dan angka2
    return hasil

# Menggunakan fungsi hitung dengan callback tambah
print(hitung(tambah, 9, 5))  # Output: 14

# Menggunakan fungsi hitung dengan callback kurang
print(hitung(kurang, 9, 5))  # Output: 4

# ==============================================================================================
#