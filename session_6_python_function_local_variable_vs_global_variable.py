# =============================================================================================
# Local Variable vs Global Variable
# Definisi fungsi dengan variabel lokal
def total(x, y):
    # z adalah variabel lokal yang hanya bisa diakses di dalam fungsi ini
    z = x + y
    return z

# Memanggil fungsi total dan mencetak hasilnya
print(total(4, 5))  # Output: 9

# Mencoba mencetak variabel z di luar fungsi
# Ini akan menghasilkan error karena z adalah variabel lokal
# print(z)  # Error

# =============================================================================================
# Local Variable vs Global Variable (2)
# Global Variable
a = 10  # Ini adalah variabel global karena didefinisikan di luar fungsi

def fungsi1():
    # Local Variable
    b = 5  # Ini adalah variabel lokal karena didefinisikan di dalam fungsi
    print("Di dalam fungsi1, a (global) =", a)  # Mengakses variabel global
    print("Di dalam fungsi1, b (local) =", b)   # Mengakses variabel lokal

def fungsi2():
    # Menggunakan keyword global untuk memodifikasi variabel global
    global a
    a = 20  # Mengubah nilai variabel global a
    print("Di dalam fungsi2, a (global) diubah menjadi =", a)

# Memanggil fungsi1 dan fungsi2
fungsi1()
print("Nilai a setelah memanggil fungsi1 =", a)  # a tetap 10

fungsi2()
print("Nilai a setelah memanggil fungsi2 =", a)  # a berubah menjadi 20

# Mencoba mengakses variabel lokal di luar fungsi
try:
    print("Nilai b di luar fungsi1 =", b)  # Ini akan menyebabkan error
except NameError as e:
    print("Error:", e)

# =============================================================================================
# Local Variable vs Global Variable (3)
# Script Python untuk Contoh 1
def coba():
    # Menggunakan variabel global x di dalam fungsi
    print(x + 2)  # Mengakses x dari luar fungsi dan menambahkan 2
    return x + 3  # Mengakses x dari luar fungsi dan menambahkan 3

# Variabel global x
x = 5
print(coba(), x)  # Output: 7 5

# Script Python untuk Contoh 2
def coba():
    x = 8  # Variabel lokal x hanya berlaku di dalam fungsi ini
    print(x + 2)  # Menggunakan variabel lokal x di dalam fungsi dan menambahkan 2
    return x + 3  # Menggunakan variabel lokal x di dalam fungsi dan menambahkan 3

# Variabel global x
x = 5
print(coba(), x)  # Output: 10 5

# =============================================================================================
# Local Variable vs Global Variable (4)

# Script Python untuk Contoh 1
def coba():
    x += 8  # Error karena mencoba memodifikasi variabel global tanpa deklarasi global
    print(x + 2)
    return x + 3

x = 5
print(coba(), x)  # Ini akan menghasilkan error

# Script Python untuk Contoh 2
def coba():
    x = 2  # Variabel lokal x di dalam fungsi
    x += 8
    print(x + 2)  # Output: 12
    return x + 3  # Output: 13

x = 5
print(coba(), x)  # Output: 13 5


# Script Python untuk Contoh 3
def coba():
    global x  # Menyatakan bahwa x adalah variabel global
    x += 8    # Modifikasi variabel global x
    print(x + 2)  # Output: 15
    return x + 3  # Output: 16

x = 5
print(coba(), x)  # Output: 16 13

# =============================================================================================
#