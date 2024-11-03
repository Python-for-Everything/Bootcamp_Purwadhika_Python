# =============================================================================================
# Menu 1. Menampilkan Daftar Buah &
# Menu 5. Exit Program

# Data awal daftar buah
buah = {
    0: {'nama': 'Apel', 'stock': 20, 'harga': 10000},
    1: {'nama': 'Jeruk', 'stock': 15, 'harga': 15000},
    2: {'nama': 'Anggur', 'stock': 25, 'harga': 20000}
}


# Fungsi untuk menampilkan daftar buah
def tampilkan_daftar_buah():
    print("\nDaftar Buah")
    print("Index\tNama\tStock\tHarga")
    for index, info_buah in buah.items():
        print(f"{index}\t{info_buah['nama']}\t{info_buah['stock']}\t{info_buah['harga']}")


# Fungsi utama untuk menampilkan menu dan menjalankan pilihan
def menu():
    while True:
        print("\nSelamat Datang di Pasar Buah")
        print("List Menu:")
        print("1. Menampilkan Daftar Buah")
        print("2. Menambah Buah")
        print("3. Menghapus Buah")
        print("4. Membeli Buah")
        print("5. Exit Program")

        try:
            pilihan = int(input("Masukkan angka Menu yang ingin dijalankan: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka 1-5.")
            continue

        if pilihan == 1:
            tampilkan_daftar_buah()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Menu belum tersedia. Silakan pilih menu lain.")


# Menjalankan program
menu()
print()
# ================================================================================================
# Menu 2. Menambah Buah
# Data awal daftar buah
buah = {
    0: {'nama': 'Apel', 'stock': 20, 'harga': 10000},
    1: {'nama': 'Jeruk', 'stock': 15, 'harga': 15000},
    2: {'nama': 'Anggur', 'stock': 25, 'harga': 20000}
}


# Fungsi untuk menampilkan daftar buah
def tampilkan_daftar_buah():
    print("\nDaftar Buah")
    print("Index\tNama\tStock\tHarga")
    for index, info_buah in buah.items():
        print(f"{index}\t{info_buah['nama']}\t{info_buah['stock']}\t{info_buah['harga']}")


# Fungsi untuk menambah buah baru ke dalam dictionary
def tambah_buah():
    nama_buah = input("Masukkan Nama Buah: ")
    try:
        stock_buah = int(input("Masukkan Stock Buah: "))
        harga_buah = int(input("Masukkan Harga Buah: "))
    except ValueError:
        print("Stock dan harga harus berupa angka. Silakan coba lagi.")
        return

    # Menentukan index baru sebagai kunci dictionary
    index_baru = max(buah.keys()) + 1 if buah else 0
    buah[index_baru] = {'nama': nama_buah, 'stock': stock_buah, 'harga': harga_buah}
    print(f"{nama_buah} berhasil ditambahkan ke dalam daftar buah.")


# Fungsi utama untuk menampilkan menu dan menjalankan pilihan
def menu():
    while True:
        print("\nSelamat Datang di Pasar Buah")
        print("List Menu:")
        print("1. Menampilkan Daftar Buah")
        print("2. Menambah Buah")
        print("3. Menghapus Buah")
        print("4. Membeli Buah")
        print("5. Exit Program")

        try:
            pilihan = int(input("Masukkan angka Menu yang ingin dijalankan: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka 1-5.")
            continue

        if pilihan == 1:
            tampilkan_daftar_buah()
        elif pilihan == 2:
            tambah_buah()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Menu belum tersedia. Silakan pilih menu lain.")


# Menjalankan program
menu()
print()
# ================================================================================================
# Menu 3. Menghapus Buah
# Data awal daftar buah
buah = {
    0: {'nama': 'Apel', 'stock': 20, 'harga': 10000},
    1: {'nama': 'Jeruk', 'stock': 15, 'harga': 15000},
    2: {'nama': 'Anggur', 'stock': 25, 'harga': 20000}
}


# Fungsi untuk menampilkan daftar buah
def tampilkan_daftar_buah():
    print("\nDaftar Buah")
    print("Index\tNama\tStock\tHarga")
    for index, info_buah in buah.items():
        print(f"{index}\t{info_buah['nama']}\t{info_buah['stock']}\t{info_buah['harga']}")


# Fungsi untuk menambah buah baru ke dalam dictionary
def tambah_buah():
    nama_buah = input("Masukkan Nama Buah: ")
    try:
        stock_buah = int(input("Masukkan Stock Buah: "))
        harga_buah = int(input("Masukkan Harga Buah: "))
    except ValueError:
        print("Stock dan harga harus berupa angka. Silakan coba lagi.")
        return

    # Menentukan index baru sebagai kunci dictionary
    index_baru = max(buah.keys()) + 1 if buah else 0
    buah[index_baru] = {'nama': nama_buah, 'stock': stock_buah, 'harga': harga_buah}
    print(f"{nama_buah} berhasil ditambahkan ke dalam daftar buah.")


# Fungsi untuk menghapus buah dari dictionary
def hapus_buah():
    tampilkan_daftar_buah()
    try:
        index_hapus = int(input("Masukkan index buah yang ingin dihapus: "))
        if index_hapus in buah:
            nama_buah = buah[index_hapus]['nama']
            del buah[index_hapus]
            print(f"{nama_buah} berhasil dihapus dari daftar buah.")
        else:
            print("Index tidak ditemukan. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka index.")


# Fungsi utama untuk menampilkan menu dan menjalankan pilihan
def menu():
    while True:
        print("\nSelamat Datang di Pasar Buah")
        print("List Menu:")
        print("1. Menampilkan Daftar Buah")
        print("2. Menambah Buah")
        print("3. Menghapus Buah")
        print("4. Membeli Buah")
        print("5. Exit Program")

        try:
            pilihan = int(input("Masukkan angka Menu yang ingin dijalankan: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka 1-5.")
            continue

        if pilihan == 1:
            tampilkan_daftar_buah()
        elif pilihan == 2:
            tambah_buah()
        elif pilihan == 3:
            hapus_buah()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Menu belum tersedia. Silakan pilih menu lain.")


# Menjalankan program
menu()
print()
# ================================================================================================
# Menu 4. Membeli Buah
# Data awal daftar buah
buah = {
    0: {'nama': 'Apel', 'stock': 20, 'harga': 10000},
    1: {'nama': 'Jeruk', 'stock': 15, 'harga': 15000},
    2: {'nama': 'Anggur', 'stock': 25, 'harga': 20000}
}


# Fungsi untuk menampilkan daftar buah
def tampilkan_daftar_buah():
    print("\nDaftar Buah")
    print("Index\tNama\tStock\tHarga")
    for index, info_buah in buah.items():
        print(f"{index}\t{info_buah['nama']}\t{info_buah['stock']}\t{info_buah['harga']}")


# Fungsi untuk menambah buah baru ke dalam dictionary
def tambah_buah():
    nama_buah = input("Masukkan Nama Buah: ")
    try:
        stock_buah = int(input("Masukkan Stock Buah: "))
        harga_buah = int(input("Masukkan Harga Buah: "))
    except ValueError:
        print("Stock dan harga harus berupa angka. Silakan coba lagi.")
        return

    index_baru = max(buah.keys()) + 1 if buah else 0
    buah[index_baru] = {'nama': nama_buah, 'stock': stock_buah, 'harga': harga_buah}
    print(f"{nama_buah} berhasil ditambahkan ke dalam daftar buah.")


# Fungsi untuk menghapus buah dari dictionary
def hapus_buah():
    tampilkan_daftar_buah()
    try:
        index_hapus = int(input("Masukkan index buah yang ingin dihapus: "))
        if index_hapus in buah:
            nama_buah = buah[index_hapus]['nama']
            del buah[index_hapus]
            print(f"{nama_buah} berhasil dihapus dari daftar buah.")
        else:
            print("Index tidak ditemukan. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka index.")


# Fungsi untuk membeli buah
def beli_buah():
    cart = []
    tampilkan_daftar_buah()

    while True:
        try:
            index_beli = int(input("Masukkan index buah yang ingin dibeli: "))
            if index_beli not in buah:
                print("Index tidak ditemukan. Silakan coba lagi.")
                continue
            jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
            if jumlah_beli > buah[index_beli]['stock']:
                print(f"Stock tidak cukup, stock {buah[index_beli]['nama']} tinggal {buah[index_beli]['stock']}")
                continue

            # Mengurangi stock buah dan menambahkan ke cart
            buah[index_beli]['stock'] -= jumlah_beli
            cart.append({
                'nama': buah[index_beli]['nama'],
                'qty': jumlah_beli,
                'harga': buah[index_beli]['harga'],
                'total': jumlah_beli * buah[index_beli]['harga']
            })
            print("Isi Cart:")
            for item in cart:
                print(f"{item['nama']}\t{item['qty']}\t{item['harga']}\t{item['total']}")

            lanjut = input("Mau beli yang lain? (y/t): ").lower()
            if lanjut != 'y':
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Menampilkan total belanja
    print("\nDaftar Belanja:")
    total_bayar = 0
    for item in cart:
        print(f"{item['nama']}\t{item['qty']}\t{item['harga']}\t{item['total']}")
        total_bayar += item['total']
    print(f"Total yang harus dibayar: {total_bayar}")

    try:
        uang = int(input("Masukkan jumlah uang yang dibayarkan: "))
        if uang < total_bayar:
            print("Uang tidak cukup untuk membayar.")
        else:
            print(f"Terima kasih! Uang kembali anda: {uang - total_bayar}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")


# Fungsi utama untuk menampilkan menu dan menjalankan pilihan
def menu():
    while True:
        print("\nSelamat Datang di Pasar Buah")
        print("List Menu:")
        print("1. Menampilkan Daftar Buah")
        print("2. Menambah Buah")
        print("3. Menghapus Buah")
        print("4. Membeli Buah")
        print("5. Exit Program")

        try:
            pilihan = int(input("Masukkan angka Menu yang ingin dijalankan: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka 1-5.")
            continue

        if pilihan == 1:
            tampilkan_daftar_buah()
        elif pilihan == 2:
            tambah_buah()
        elif pilihan == 3:
            hapus_buah()
        elif pilihan == 4:
            beli_buah()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Menu belum tersedia. Silakan pilih menu lain.")


# Menjalankan program
menu()
print()
# ================================================================================================
#