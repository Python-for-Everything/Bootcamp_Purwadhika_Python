# ==========================================================================================
# Fungsi penjumlahan
def addition(a, b):
    return a + b

# Fungsi pengurangan
def subtraction(a, b):
    return a - b

# Fungsi perkalian
def multiplication(a, b):
    return a * b

# Fungsi pembagian
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Fungsi utama yang memanggil fungsi lain dan menampilkan hasil
def showResult(a, b):
    print("Hasil Penjumlahan:", addition(a, b))
    print("Hasil Pengurangan:", subtraction(a, b))
    print("Hasil Perkalian:", multiplication(a, b))
    print("Hasil Pembagian:", division(a, b))

# Memanggil fungsi showResult dengan dua angka
showResult(10, 5)

# ==========================================================================================
#
