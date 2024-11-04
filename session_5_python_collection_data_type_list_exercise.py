print(f"Soal 1 - Find Min and Max Value")

numbers = [41, 5, 1, 3, 89, 32]

# Menemukan nilai minimum dan maksimum
min = min(numbers)
max = max(numbers)

# Tampilkan hasil
print("Numbers =", numbers)
print("Minimum value =", min)
print("Maximum value =", max)
print()

# ==============================================================================================
print(f"Soal 2 - Sort Ascending")
# List sebelum di sort = [41, 5, 1, 3, 89, 32]
# List setelah di sort = [1, 3, 5, 32, 41, 89]

numbers = [41, 5, 1, 3, 89, 32]
# List sebelum di-sort
print("List Sebelum Di Sort =", numbers)

# urutan ascending
numbers.sort()

# list setelah di-sort
print("List Setelah Di Sort =", numbers)
print()
# ==============================================================================================
print(f"Soal 3 - Cari Kata Muncul")
def hitung_kata(kalimat):
    # Ubah kalimat menjadi list kata
    kata_list = kalimat.lower().split()
    kata_count = {}

    # Hitung jumlah kata
    for kata in kata_list:
        # Capitalized kata sesuai contoh
        kata_capitalized = kata.capitalize()
        if kata_capitalized in kata_count:
            kata_count[kata_capitalized] += 1
        else:
            kata_count[kata_capitalized] = 1

    # Tampilkan hasil
    for kata, jumlah in kata_count.items():
        print(f"Jumlah kata '{kata}' ada {jumlah}")

# Kalimat contoh
kalimat = "Aku baru makan nasi terus aku mau makan mie nanti malam"
hitung_kata(kalimat)

# ==============================================================================================
print(f"Soal 4 s/d 7 - Toko Buah")

daftar_buah = [
    {"Nama": "Apel", "Stock": 20, "Harga": 10000},
    {"Nama": "Jeruk", "Stock": 15, "Harga": 15000},
    {"Nama": "Anggur", "Stock": 25, "Harga": 20000}
]

# Tampilkan daftar buah
def tampilkan_daftar_buah():
    print("\nDaftar Buah")
    print("Index | Nama     | Stock          | Harga")
    for i, buah in enumerate(daftar_buah):
        print(f"{i}     | {buah['Nama']:<8} | {buah['Stock']:<10}     | {buah['Harga']:<6}")


# Tambah buah
def tambah_buah():
    nama_buah = input("Masukkan Nama Buah: ")
    try:
        stock_buah = int(input("Masukkan Stock Buah: "))
        harga_buah = int(input("Masukkan Harga Buah: "))
    except ValueError:
        print("Input tidak valid. Pastikan Stock dan Harga adalah angka.")
        return

    # Tambah buah baru ke daftar buah
    daftar_buah.append({"Nama": nama_buah, "Stock": stock_buah, "Harga": harga_buah})
    print("\nBuah berhasil ditambahkan!")
    tampilkan_daftar_buah()

# Fungsi hapus buah
def hapus_buah():
    tampilkan_daftar_buah()
    try:
        index_hapus = int(input("Masukkan index buah yang ingin dihapus: "))
        if 0 <= index_hapus < len(daftar_buah):
            buah_dihapus = daftar_buah.pop(index_hapus)
            print(f"\nBuah {buah_dihapus['Nama']} berhasil dihapus!")
        else:
            print("Index tidak valid.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka.")

    tampilkan_daftar_buah()

# Fungsi beli buah
def membeli_buah():
    cart = []
    while True:
        tampilkan_daftar_buah()

        try:
            index_beli = int(input("\nMasukkan index buah yang ingin dibeli: "))
            jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

            # Cek stok buah
            if 0 <= index_beli < len(daftar_buah):
                buah = daftar_buah[index_beli]
                if jumlah_beli <= buah["Stock"]:
                    # Tambahkan ke cart
                    total_harga = jumlah_beli * buah["Harga"]
                    cart.append(
                        {"Nama": buah["Nama"], "Qty": jumlah_beli, "Harga": buah["Harga"], "Total Harga": total_harga})

                    # Update stok
                    buah["Stock"] -= jumlah_beli
                    print(f"Stok {buah['Nama']} cukup, stok sekarang: {buah['Stock']}")
                else:
                    print(f"Stok {buah['Nama']} tidak cukup, stok hanya {buah['Stock']}")
            else:
                print("Index buah tidak valid.")

        except ValueError:
            print("Input tidak valid. Pastikan memasukkan angka.")
            continue

        # Tanyakan apakah ingin lanjut belanja
        lanjut = input("Ingin lanjut belanja? (ya/tidak): ").lower()
        if lanjut != 'ya':
            break

    # Tampilkan rincian pembelian
    print("\nIsi Cart:")
    print("Nama     | Qty | Harga   | Total Harga")
    total_bayar = 0
    for item in cart:
        print(f"{item['Nama']} | {item['Qty']}   | {item['Harga']}  | {item['Total Harga']}")
        total_bayar += item['Total Harga']

    print("\nDetail Belanja:")
    for item in cart:
        print(f"{item['Nama']} : {item['Qty']} x {item['Harga']} = {item['Total Harga']}")
    print(f"Total yang harus dibayar: {total_bayar}")

    # Pembayaran
    while True:
        try:
            uang_dibayar = int(input("Masukkan jumlah uang yang dibayar: "))
            if uang_dibayar >= total_bayar:
                kembalian = uang_dibayar - total_bayar
                print(f"Uang kembali anda: {kembalian}")
                print("Terima kasih telah berbelanja!")
                break
            else:
                kurang = total_bayar - uang_dibayar
                print(f"Uang anda kurang sebesar {kurang}")
        except ValueError:
            print("Input tidak valid. Pastikan memasukkan angka.")

# Fungsi utama
def menu():
    while True:
        print("\nSelamat Datang di Pasar Buah")
        print("List Menu:")
        print("1. Menampilkan Daftar Buah")
        print("2. Menambah Buah")
        print("3. Menghapus Buah")
        print("4. Membeli Buah")
        print("5. Exit Program")

        pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")

        if pilihan == "1":
            tampilkan_daftar_buah()
        elif pilihan == "2":
            tambah_buah()
        elif pilihan == "3":
            hapus_buah()
        elif pilihan == "4":
            membeli_buah()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan belum tersedia atau salah. Silakan coba lagi.")


# Jalankan program
menu()

# ====================================================================================================


