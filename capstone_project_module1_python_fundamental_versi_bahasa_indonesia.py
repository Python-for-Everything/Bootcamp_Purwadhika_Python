hardware_db = {}  # Penyimpanan data perangkat keras

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        print("\n=== Aplikasi Manajemen Perangkat Keras Jaringan ===")
        print("1. Lihat Perangkat Keras")
        print("2. Tambah Perangkat Keras")
        print("3. Perbarui Perangkat Keras")
        print("4. Hapus Perangkat Keras")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            view_hardware_menu()
        elif choice == '2':
            add_hardware_menu()
        elif choice == '3':
            update_hardware_menu()
        elif choice == '4':
            delete_hardware_menu()
        elif choice == '5':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi yang Anda masukkan tidak valid.")

# Fungsi untuk menampilkan menu lihat perangkat keras
def view_hardware_menu():
    if not hardware_db:
        print("Data perangkat keras tidak ada.")
    else:
        print("\n=== Menu Lihat Perangkat Keras ===")
        print("1. Tampilkan Semua Data")
        print("2. Cari Data Berdasarkan Kunci Utama")
        choice = input("Pilih opsi (1-2): ")

        if choice == '1':
            display_all_data()
        elif choice == '2':
            search_hardware_by_primary_key()
        else:
            print("Opsi yang Anda masukkan tidak valid.")

# Fungsi untuk menampilkan semua data
def display_all_data():
    print("\nDaftar Perangkat Keras:")
    for key, data in hardware_db.items():
        print(f"ID: {key}, Detail: {data}")

# Fungsi untuk mencari data berdasarkan kunci utama
def search_hardware_by_primary_key():
    primary_key = input("Masukkan Kunci Utama Perangkat Keras: ")
    if primary_key in hardware_db:
        print(f"Data Perangkat Keras {primary_key}: {hardware_db[primary_key]}")
    else:
        print("Data tidak ditemukan.")

# Fungsi untuk menampilkan menu tambah perangkat keras
def add_hardware_menu():
    primary_key = input("Masukkan Kunci Utama Perangkat Keras: ")
    if primary_key in hardware_db:
        print("Data sudah ada.")
    else:
        hardware_data = input("Masukkan Detail Perangkat Keras: ")
        hardware_db[primary_key] = hardware_data
        print("Data berhasil disimpan.")

# Fungsi untuk menampilkan menu pembaruan perangkat keras
def update_hardware_menu():
    primary_key = input("Masukkan Kunci Utama Perangkat Keras untuk Diperbarui: ")
    if primary_key in hardware_db:
        print(f"Data saat ini: {hardware_db[primary_key]}")
        new_data = input("Masukkan data baru untuk diperbarui: ")
        hardware_db[primary_key] = new_data
        print("Data berhasil diperbarui.")
    else:
        print("Data yang Anda cari tidak ada.")

# Fungsi untuk menampilkan menu hapus perangkat keras
def delete_hardware_menu():
    primary_key = input("Masukkan Kunci Utama Perangkat Keras untuk Dihapus: ")
    if primary_key in hardware_db:
        del hardware_db[primary_key]
        print("Data berhasil dihapus.")
    else:
        print("Data yang Anda cari tidak ada.")

# Jalankan menu utama
main_menu()
