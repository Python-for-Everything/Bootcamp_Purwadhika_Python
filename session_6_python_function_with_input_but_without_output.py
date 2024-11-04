# Function With Input but Without Output
# Definisi fungsi dengan input tapi tanpa output
def salamBalik(nama, usia):
    # Menggunakan format string untuk menampilkan nama dan usia
    print("Hello, perkenalkan nama saya {}, dan usia saya {}".format(nama, usia))
    print("Senang bertemu dengan anda!")

# Pemanggilan fungsi dengan parameter
salamBalik("Andi", 25)
salamBalik("Budi", 27)

# ==============================================================================================
# Parameter or Argument ?
# Definisi fungsi dengan parameter 'nama' dan 'usia'
def salamBalik(nama, usia):
    # Menggunakan format string untuk menampilkan nama dan usia
    print("Hello, perkenalkan nama saya {}, dan usia saya {}".format(nama, usia))
    print("Senang bertemu dengan anda!")

# Memanggil fungsi salamBalik dengan argument 'Andi' dan 25
salamBalik("Andi", 25)

# ==============================================================================================
# Parameter or Argument (2) ?
# Definisi fungsi dengan parameter 'nama' dan 'usia'
def salamBalik(nama, usia):
    # Menggunakan format string untuk menampilkan nama dan usia
    print("Hello, perkenalkan nama saya {}, dan usia saya {}".format(nama, usia))
    print("Senang bertemu dengan anda!")

# Pemanggilan fungsi dengan keyword arguments
salamBalik(usia=25, nama="Andi")

# ==============================================================================================
#
