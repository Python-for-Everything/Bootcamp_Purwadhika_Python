# Inisialisasi data kendaraan
vehicles = [
    {"id": 1, "jenis": "Mobil", "nama": "Toyota Avanza", "harga": 250000000, "stok": 5},
    {"id": 2, "jenis": "Motor", "nama": "Yamaha NMax", "harga": 30000000, "stok": 15}
]


# Fungsi menampilkan semua kendaraan
def show_vehicles():
    print("Data Kendaraan Toko:")
    print("ID\tJenis\tNama\t\t\tHarga\t\tStok")
    for vehicle in vehicles:
        print(f"{vehicle['id']}\t{vehicle['jenis']}\t{vehicle['nama']}\tRp {vehicle['harga']}\t{vehicle['stok']}")


# Fungsi menambahkan kendaraan baru
def add_vehicle():
    id = int(input("Masukkan ID kendaraan: "))
    jenis = input("Masukkan jenis kendaraan (Mobil/Motor): ")
    nama = input("Masukkan nama kendaraan: ")
    harga = int(input("Masukkan harga kendaraan: "))
    stok = int(input("Masukkan stok kendaraan: "))
    vehicles.append({"id": id, "jenis": jenis, "nama": nama, "harga": harga, "stok": stok})
    print("Kendaraan berhasil ditambahkan!")


# Fungsi mengubah data kendaraan
def update_vehicle():
    id = int(input("Masukkan ID kendaraan yang akan diubah: "))
    for vehicle in vehicles:
        if vehicle['id'] == id:
            print("Data kendaraan ditemukan. Silakan ubah informasi:")
            vehicle['jenis'] = input("Masukkan jenis kendaraan baru (Mobil/Motor): ")
            vehicle['nama'] = input("Masukkan nama kendaraan baru: ")
            vehicle['harga'] = int(input("Masukkan harga kendaraan baru: "))
            vehicle['stok'] = int(input("Masukkan stok kendaraan baru: "))
            print("Data kendaraan berhasil diubah!")
            return
    print("Kendaraan dengan ID tersebut tidak ditemukan.")


# Fungsi menghapus kendaraan
def delete_vehicle():
    id = int(input("Masukkan ID kendaraan yang akan dihapus: "))
    for vehicle in vehicles:
        if vehicle['id'] == id:
            vehicles.remove(vehicle)
            print("Kendaraan berhasil dihapus!")
            return
    print("Kendaraan dengan ID tersebut tidak ditemukan.")


# Fungsi utama
def main():
    while True:
        print("\nMenu:")
        print("1. Lihat Kendaraan")
        print("2. Tambah Kendaraan")
        print("3. Ubah Kendaraan")
        print("4. Hapus Kendaraan")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            show_vehicles()
        elif pilihan == "2":
            add_vehicle()
        elif pilihan == "3":
            update_vehicle()
        elif pilihan == "4":
            delete_vehicle()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Jalankan program
main()
