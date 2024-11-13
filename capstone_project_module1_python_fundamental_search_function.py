# Aplikasi Manajemen Perangkat Keras Jaringan dengan Fitur Pencarian

# Penyimpanan data contoh
daftar_perangkat = []


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


def tampilkan_semua_perangkat():
    print("\nSemua Data Perangkat:")
    for item in daftar_perangkat:
        print(item)


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


def menu_cari_perangkat():
    if not daftar_perangkat:
        print("Data tidak ada.")
        return

    print("\nMenu Cari Perangkat")
    id_perangkat = input("Masukkan ID perangkat untuk dicari: ")
    for item in daftar_perangkat:
        if item['id'] == id_perangkat:
            print("Perangkat Ditemukan:", item)
            return
    print("Tidak ada data dengan ID perangkat tersebut.")


# Menjalankan aplikasi
menu_utama()
