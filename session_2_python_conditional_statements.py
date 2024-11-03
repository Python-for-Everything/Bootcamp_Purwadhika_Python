""" Exercise Conditional Statement"""
""" Soal 1"""
# Input dari User
angka = int(input("Masukkan Angka: "))

# Cek Angka Ganjil atau Genap
if angka % 2 == 0:
    print(f"Angka {angka} tergolong Angka Genap!")
else:
    print(f"\nAngka {angka} tergolong Angka Ganjil!")
print()
# ====================================================================================================
""" Exercise Conditional Statement"""
""" Soal 2 """
print(f"*** Hitung Index Masa Tubuh (IMT) ***")

# Input Berat Badan (Kg)
berat_badan = float(input("Masukkan Berat Badan (Kg): "))

# Input Tinggi Badan & Convert centimeter ke meter
tinggi_badan = float(input("Masukkan Tinggi (cm): ")) / 100

# Hitung IMT dengan Rumus Berat_Badan / (tinggi ** 2)
imt = berat_badan / (tinggi_badan ** 2)

# Nilai IMT (2 angka decimal)
print(f"Berat {berat_badan} kg dan Tinggi {tinggi_badan:} meter")
print(f"IMT = {imt:.2f}")

# Kategori IMT
if imt < 18.5:
    kategori = "Berat Badan Kurang"
elif 18.5 <= imt < 25:
    kategori = "Berat Badan Ideal"
elif 25 <= imt < 30:
    kategori = "Berat Badan Berlebih"
elif 30 <= imt < 40:
    kategori = "Berat Badan Sangat Berlebih"
else:
    kategori = "Obesitas"

# Kategori IMT
print(f"IMT = {imt:.2f}, {kategori}!")
print()
# ====================================================================================================
""" Exercise Conditional Statement"""
""" Soal 3 """
print(f"*** Hitung Harga Buah ***")
# Harga per buah
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

# Input jumlah buah
jumlah_apel = int(input("Masukkan Jumlah Apel: "))
jumlah_jeruk = int(input("Masukkan Jumlah Jeruk: "))
jumlah_anggur = int(input("Masukkan Jumlah Anggur: "))

# Hitung total biaya setiap buah
total_apel = jumlah_apel * harga_apel
total_jeruk = jumlah_jeruk * harga_jeruk
total_anggur = jumlah_anggur * harga_anggur

# Hitung total keseluruhan
total_belanja = total_apel + total_jeruk + total_anggur

# Detail belanja
print("\nDetail Belanja")
print(f"Apel : {jumlah_apel} x {harga_apel} = {total_apel}")
print(f"Jeruk : {jumlah_jeruk} x {harga_jeruk} = {total_jeruk}")
print(f"Anggur : {jumlah_anggur} x {harga_anggur} = {total_anggur}")
print(f"Total : {total_belanja}")

# Jumlah uang
jumlah_uang = int(input("\nMasukkan jumlah uang: "))

# Cek Pembayaran
if jumlah_uang < total_belanja:
    kekurangan = total_belanja - jumlah_uang
    print(f"Transaksi anda dibatalkan, uangnya kurang sebesar {kekurangan}")
elif jumlah_uang == total_belanja:
    print("Terima kasih")
else:
    kembalian = jumlah_uang - total_belanja
    print("Terima kasih")
    print(f"Uang kembali anda : {kembalian}")
print()
# ====================================================================================================
