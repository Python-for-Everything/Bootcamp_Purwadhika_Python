# Inisialisasi data produk (sebagai contoh awal)
products = [
    {"id": 1, "nama": "Laptop", "harga": 15000000, "stok": 10},
    {"id": 2, "nama": "Smartphone", "harga": 7000000, "stok": 20},
    {"id": 3, "nama": "Tablet", "harga": 4000000, "stok": 15}
]


# Fungsi menampilkan semua produk
def show_products():
    print("Data Produk Toko Elektronik:")
    print("ID\tNama\t\tHarga\t\tStok")
    for product in products:
        print(f"{product['id']}\t{product['nama']}\t\tRp {product['harga']}\t{product['stok']}")


# Fungsi menambahkan produk baru
def add_product():
    id = int(input("Masukkan ID produk: "))
    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))
    products.append({"id": id, "nama": nama, "harga": harga, "stok": stok})
    print("Produk berhasil ditambahkan!")


# Fungsi mengubah data produk
def update_product():
    id = int(input("Masukkan ID produk yang akan diubah: "))
    for product in products:
        if product['id'] == id:
            print("Data produk ditemukan. Silakan ubah informasi:")
            product['nama'] = input("Masukkan nama produk baru: ")
            product['harga'] = int(input("Masukkan harga produk baru: "))
            product['stok'] = int(input("Masukkan stok produk baru: "))
            print("Data produk berhasil diubah!")
            return
    print("Produk dengan ID tersebut tidak ditemukan.")


# Fungsi menghapus produk
def delete_product():
    id = int(input("Masukkan ID produk yang akan dihapus: "))
    for product in products:
        if product['id'] == id:
            products.remove(product)
            print("Produk berhasil dihapus!")
            return
    print("Produk dengan ID tersebut tidak ditemukan.")


# Fungsi utama
def main():
    while True:
        print("\nMenu:")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            show_products()
        elif pilihan == "2":
            add_product()
        elif pilihan == "3":
            update_product()
        elif pilihan == "4":
            delete_product()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Jalankan program
main()
