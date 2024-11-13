# Aplikasi Management Perangkat Keras Jaringan Dengan Fitur Pencarian

# Penyimpanan data contoh
daftar_perangkat = {
    0: {"firewall": "Cisco ASA", "Qty": 2, "Harga": 1000000.00},
    1: {"firewall": "Fortigate", "Qty": 2, "Harga": 500000000},
    2: {"firewall": "Check Point", "Qty": 2, "Harga": 1000000000},
    3: {"firewall": "Sophos XG Firewall", "Qty": 2, "Harga": 1000000.00},
    4: {"firewall": "Paloalto Networks", "Qty": 2, "Harga": 2000000000},
    5: {"firewall": "Juniper SRX", "Qty": 2, "Harga": 1000000000},
    6: {"router": "Cisco ISR", "Qty": 2, "Harga": 1000000000},
    7: {"router": "Fortinet Switch", "Qty": 2, "Harga": 1000000000},
    8: {"router": "Juniper MX", "Qty": 2, "Harga": 1000000000},
    9: {"wifi_controller": "Cisco WLC", "Qty": 2, "Harga": 2000000000},
    10: {"wifi_controller": "Fortinet WLC", "Qty": 2, "Harga": 1000000000},
    11: {"access_point": "Cisco Aironet", "Qty": 2, "Harga": 2000000000},
    12: {"access_point": "Aruba Controller", "Qty": 2, "Harga": 2000000000},
    13: {"load_balancer": "Cisco Nexus Load Balancer", "Qty": 2, "Harga": 2000000000},
    14: {"load_balancer": "F5", "Qty": 2, "Harga": 2000000000},
    15: {"vpn_gateway": "Cisco AnyConnect", "Qty": 2, "Harga": 2000000000},
    16: {"vpn_gateway": "Fortigate VPN", "Qty": 2, "Harga": 1000000000},
    17: {"vpn_gateway": "Sophos XG Firewall", "Qty": 2, "Harga": 2000000000},
    18: {"ids_ips": "Cisco Firepower", "Qty": 2, "Harga": 2000000000},
    19: {"ids_ips": "Fortigate IPS", "Qty": 2, "Harga": 2000000000},
    20: {"utm_appliance": "Cisco Meraki", "Qty": 2, "Harga": 2000000000},
    21: {"utm_appliance": "Fortigate UTM", "Qty": 2, "Harga": 2000000000},
    22: {"utm_appliance": "CheckPoint UTM", "Qty": 2, "Harga": 2000000000},
    23: {"utm_appliance": "Sophos XG UTM", "Qty": 2, "Harga": 2000000000},
}

# Fungsi tampilkan menu utama dan jalankan pilihan
def menu_utama():
    while True:
        print("\nManajemen Perangkat Keras Jaringan")
        print("1. Lihat Perangkat")
        print("2. Tambah Perangkat")
        print("3. Perbarui Perangkat")
        print("4. Hapus Perangkat")
        print("5. Cari Perangkat")
        print("6. Keluar")

        pilihan = input("Pilih opsi: ")
        if pilihan == '1':
            menu_baca_perangkat()
        elif pilihan == '2':
            menu_tambah_perangkat()
        elif pilihan == '3':
            menu_perbarui_perangkat()
        elif pilihan == '4':
            menu_hapus_perangkat()
        elif pilihan == '5':
            menu_cari_perangkat()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")


# Fungsi Menu untuk Baca Perangkat
def menu_baca_perangkat():
    if not daftar_perangkat:
        print("Data tidak ada.")
        return

    print("\nMenu Baca Perangkat")
    print("1. Tampilkan Semua Data")
    print("2. Kembali ke Menu Utama")

    pilihan = input("Pilih opsi: ")
    if pilihan == '1':
        tampilkan_semua_perangkat()
    elif pilihan == '2':
        return
    else:
        print("Opsi tidak valid. Kembali ke menu utama.")


# Fungsi Menu untuk Tampilkan Semua Perangkat
def tampilkan_semua_perangkat():
    print("\nSemua Data Perangkat:")
    for item in daftar_perangkat:
        print(item)


# Fungsi Menu untuk Tambah Perangkat
def menu_tambah_perangkat():
    print("\nMenu Tambah Perangkat")
    id_perangkat = input("Masukkan ID perangkat: ")
    if any(item['id'] == id_perangkat for item in daftar_perangkat):
        print("Data sudah ada.")
        return
    nama_perangkat = input("Masukkan nama perangkat: ")
    jenis_perangkat = input("Masukkan jenis perangkat: ")

    perangkat_baru = {
        'id': id_perangkat,
        'nama': nama_perangkat,
        'jenis': jenis_perangkat
    }
    simpan_data = input("Simpan data? (ya/tidak): ").lower()
    if simpan_data == 'ya':
        daftar_perangkat.append(perangkat_baru)
        print("Data berhasil disimpan.")
    else:
        print("Data tidak disimpan.")


# Fungsi Menu untuk Perbaharui Perangkat
def menu_perbarui_perangkat():
    if not daftar_perangkat:
        print("Data tidak ada.")
        return

    print("\nMenu Perbarui Perangkat")
    id_perangkat = input("Masukkan ID perangkat untuk diperbarui: ")
    for item in daftar_perangkat:
        if item['id'] == id_perangkat:
            print("Data Saat Ini:", item)
            perbarui = input("Apakah Anda ingin melanjutkan pembaruan? (ya/tidak): ").lower()
            if perbarui == 'ya':
                kolom_diperbarui = input("Masukkan kolom yang akan diperbarui (nama/jenis): ").lower()
                if kolom_diperbarui in item:
                    nilai_baru = input("Masukkan nilai baru: ")
                    item[kolom_diperbarui] = nilai_baru
                    print("Data berhasil diperbarui.")
                else:
                    print("Kolom tidak valid.")
            return
    print("Data yang Anda cari tidak ada.")


# Fungsi Menu untuk Hapus Perangkat
def menu_hapus_perangkat():
    if not daftar_perangkat:
        print("Data tidak ada.")
        return

    print("\nMenu Hapus Perangkat")
    id_perangkat = input("Masukkan ID perangkat untuk dihapus: ")
    for item in daftar_perangkat:
        if item['id'] == id_perangkat:
            konfirmasi = input("Apakah Anda ingin menghapus data ini? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                daftar_perangkat.remove(item)
                print("Data berhasil dihapus.")
            return
    print("Data yang Anda cari tidak ada.")


# Fungsi Menu untuk Cari Perangkat
def menu_cari_perangkat():
    if not daftar_perangkat:
        print("Data tidak ada.")
        return

    print("\nMenu Cari Perangkat")
    try:
        id_perangkat = int(input("Masukkan ID perangkat untuk dicari: "))
    except ValueError:
        print("ID perangkat harus berupa angka.")
        return

    for item in daftar_perangkat:
        if item['id'] == id_perangkat:
            print("Perangkat Ditemukan:", item)
            return
    print("Tidak ada data dengan ID perangkat tersebut.")


# Menjalankan aplikasi
menu_utama()