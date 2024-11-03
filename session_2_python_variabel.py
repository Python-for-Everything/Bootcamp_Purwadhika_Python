# Slide 1
# Data Science - Session 3
# Python Variable, Data Types, and USer Input
# Exercise_Module1_Day2

# Soal 1
x = 4
y = 3
z = 2

# Hitung Nilai
w = (x + y * z) / (x * y) ** 2

# Menampilkan hasil
print(f"\nNilai w adalah: {w}")
# ===============================================================================================
# Soal 2
# Silahkan masukkan angka berapapun : 5
# Kuadrat dari 5 = 25

angka = input('Masukkan angka berpapapun: ')    # ini masih string
hasilKuadrat = int(angka) **2                    # ini tipe datanya integer

print(f'Kuadrat dari {angka} = {hasilKuadrat}')

# ===============================================================================================
# Soal 3
# 485 hari.
# Nyatakan dalam tahun, bulan, minggu dan hari.
# * 1 bulan = 30 hari, 1 tahun = 360 hari.

jumlahHari = int(input('Masukkan jumlah hari: '))     # 485
print(jumlahHari)

tahun = jumlahHari // 360         # 485//360 = 1
sisaHari = jumlahHari % 360         # 125

bulan = sisaHari // 30            # 125//30 = 4
sisaHari = sisaHari % 30            # 5

minggu = sisaHari // 7            # 5 // 7 = 0
sisaHari = sisaHari % 7             # 5

hari = sisaHari                   # 5

print(f'{jumlahHari} hari terdiri dari {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')
print(tahun, "tahun", bulan, "bulan")
# ===============================================================================================
# Soal 4
# Saat ini, jumlah usia Andi & Budi = 49 th,
# dengan rasio Usia Andi & Budi = 0.4
# Berapakah usia Andi & Budi dalam 2 tahun mendatang ?

rasioAndi = 4
rasioBudi = 10

totalRasio = rasioAndi + rasioBudi
totalUmur = 49

umurAndi = int((rasioAndi / totalRasio) * totalUmur)
umurBudi = int((rasioBudi / totalRasio) * totalUmur)

print(f'Umur Andi sekarang adalah {umurAndi} tahun')
print(f'Umur Budi sekarang adalah {umurBudi} tahun')

print(f'Umur Andi 2 tahun lagi adalah {umurAndi+2} tahun')
print(f'Umur Budi 2 tahun lagi adalah {umurBudi+2} tahun')

# ===============================================================================================
# Soal 5
# Jarak Mobil A & B = 120 km.
# A berjalan 60 km/h dari timur.
# B berjalan 40 km/h dari barat.
# A & B start pukul 9 WIB.
# Jam berapa A & B bertabrakan ?

jarak = 120             # km
kecA = 60/3600          # km/detik
kecB = 40/3600          # km/detik
start = 9               # satuan jam

# setiap 3600 detik, mobil akan saling mendekat 100 km
# setiap 1 detik, mobil mendekat 100/3600

jarakPerDetik = kecA + kecB
print(f'Jarak per detik saling mendekat adalah {jarakPerDetik}')

# untuk terjadi tabrakan, jarak total mendekat harus 120 km

detikTabrakan = jarak/ jarakPerDetik
print(f'Tabrakan terjadi setelah {detikTabrakan} detik')

jam = int(detikTabrakan // 3600)
sisaDetik = detikTabrakan % 3600

menit = int(sisaDetik // 60)
sisaDetik = sisaDetik% 60

detik = int(sisaDetik)

print(f'Tabrakan Terjadi Pada Pukul {start+jam}:{menit}:{detik}')

# ===============================================================================================
# Soal 6
# Masukkan Jumlah Apel : 2
# Masukkan Jumlah Jeruk : 3
# Masukkan Jumlah Anggur : 5
# Detail Belanja
# Apel : 2 x 10000 = 20000
# Jeruk : 3 x 15000 = 45000
# Anggur : 5 x 20000 = 10000

jmlApel = int(input('Masukkan jumlah apel: '))
jmlJeruk = int(input('Masukkan jumlah jeruk: '))
jmlAnggur = int(input('Masukkan jumlah anggur: '))

# Diketahui harga buah sebagai berikut:
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

print('Detail Belanja')

print(f'Apel: \t {jmlApel} x {hargaApel} = {jmlApel*hargaApel}')
print(f'Jeruk: \t {jmlJeruk} x {hargaJeruk} = {jmlJeruk*hargaJeruk}')
print(f'Anggur:\t {jmlAnggur} x {hargaAnggur} = {jmlAnggur*hargaAnggur}')

totalBelanja = (jmlApel*hargaApel) + (jmlJeruk*hargaJeruk) + (jmlAnggur*hargaAnggur)
print(f'Total belanjaan Anda Rp.{totalBelanja}')

# ===============================================================================================
#

