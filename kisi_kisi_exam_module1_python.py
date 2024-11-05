# =============================================================================================
# Soal 1
# 1. Jika terdapat kalimat:
# 'Manusia biasa ini sangat istimewa;
# Maka untuk mengecek apakah terdapat karakter 'isti' pada kalimat tersebut adalah dengan menggunakan . . . .
# a. in --> Jawaban
# b. at
# c. on
# d. go
# e. check

# Jawaban :
# Jawaban yang benar adalah: a. in
#
# Penjelasan
# Di dalam Python, operator in digunakan untuk memeriksa apakah suatu substring ada di dalam string lain.
# Jadi, jika kita ingin mengetahui apakah substring 'isti' ada dalam kalimat 'Manusia biasa ini sangat istimewa',
# kita dapat menggunakan operator in.
#
# Operator in mengembalikan nilai True jika substring tersebut ditemukan dalam string, dan False jika tidak ditemukan.
#
# Script Python
# Berikut adalah script Python untuk memeriksa apakah substring 'isti' terdapat dalam kalimat yang diberikan:

# Kalimat yang akan diperiksa
import string

kalimat = 'Manusia biasa ini sangat istimewa'

# Memeriksa apakah 'isti' ada dalam kalimat
if 'isti' in kalimat:
    print("Substring 'isti' ditemukan dalam kalimat.")
else:
    print("Substring 'isti' tidak ditemukan dalam kalimat.")

# Output
# Script ini akan menghasilkan output:
#
# Substring 'isti' ditemukan dalam kalimat.
#
# Penjelasan Script
# kalimat: Kita mendefinisikan variabel kalimat dengan nilai 'Manusia biasa ini sangat istimewa'.
# Pengecekan dengan in: Menggunakan if 'isti' in kalimat untuk memeriksa apakah substring 'isti' ada di dalam kalimat.
# Output: Jika substring 'isti' ditemukan, maka program mencetak bahwa substring ditemukan; jika tidak,
# program mencetak bahwa substring tidak ditemukan.
# Jadi, jawaban yang benar adalah a. in, karena in adalah operator yang digunakan dalam Python
# untuk memeriksa apakah suatu substring ada di dalam string.
# =============================================================================================
# Soal 2
# 2. Yang merupakan fungsi dari 'Break' pada looping statement adalah . . . .
#    a. Melanjutkan ke loop value berikutnya: continue
#    b. Memberhentikan program: exit
#    c. Menampilkan output program: print
#    d. Memberhentikan proses looping : Break --> Jawaban
#    e. Semua jawaban salah

# Jawaban yang benar adalah: d. Memberhentikan proses looping : Break
#
# Penjelasan
# Di dalam Python, statement break digunakan untuk menghentikan atau keluar dari loop (baik itu for atau while)
# saat kondisi tertentu terpenuhi. Ketika break dieksekusi, Python langsung menghentikan loop yang sedang berjalan dan
# melanjutkan eksekusi kode di luar loop tersebut.

# =============================================================================================
# Soal 3
# 3. Berikut ini fungsi cari continue pada looping statements adalah . . . .
#    a. Emang ada fungsi continue?
#    b. Melompati (skip) suatu kondisi yang dikehendaki dan lanjut pada kondisi berikutnya --> Jawaban
#    c. Melanjutkan ke output
#    d. Melanjutkan ke fungsi selanjutnya
#    e. Memberhentikan paksa program
#
# Jawaban yang benar adalah: b. Melompati (skip) suatu kondisi yang dikehendaki dan lanjut pada kondisi berikutnya
#
# Penjelasan
# Di dalam Python, statement continue digunakan dalam loop (for atau while) untuk melewatkan iterasi saat ini
# dan langsung melanjutkan ke iterasi berikutnya. Jika kondisi tertentu terpenuhi di dalam loop,
# dan kita tidak ingin mengeksekusi sisa kode dalam iterasi tersebut,
# kita bisa menggunakan continue untuk melompati ke iterasi berikutnya.
# =============================================================================================
# Soal 4
# 4. Jika terdapat kalimat:
# '  Purwadhika adalah tempatku belajar coding untuk menjadi seorang Data Scientist'
#    Maka untuk menemukan kata coding terdapat pada index keberapa, perintah yang digunakan adalah . . . .
#    a. .find()   --> Jawaban
#    b. .index()  --> Jawaban
#    c. .check_index()
#    d. .index_position()
#    e. .where()

# Jawaban yang benar adalah: a. .find() atau b. .index()
#
# Penjelasan
# Di dalam Python, untuk menemukan posisi atau indeks dari suatu substring dalam string,
# kita bisa menggunakan metode .find() atau .index(). Keduanya berfungsi untuk mencari
# posisi kemunculan pertama dari substring yang dicari.
#
# .find(): Mengembalikan indeks dari kemunculan pertama substring dalam string.
# Jika substring tidak ditemukan, .find() akan mengembalikan -1, sehingga lebih aman digunakan
# jika ada kemungkinan substring tidak ditemukan.
# .index(): Sama seperti .find(), mengembalikan indeks dari kemunculan pertama substring dalam string.
# Namun, jika substring tidak ditemukan, .index() akan menghasilkan error (ValueError).
# Jadi, kedua metode ini bisa digunakan untuk menemukan posisi kata "coding" dalam kalimat tersebut.
# =============================================================================================
# Soal 5
# 5. Jika terdapat list :
#    nama = ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda']
#    Maka untuk menambahkan 'Rifa' dapat digunakan cara sebagai berikut, kecuali . . . .
#    a. nama.append('Rifa') : menambahkan data baru sekaligus di posisi terkahir
#    b. nama.pop('Rifa') : menghapus item  --> Jawaban
#    c. nama.insert(1, 'Rifa') : menambahkan data baru sesuai index
#    d. nama.insert('Rifa') : karena perlu define index --> Jawaban
#    e. nama.extend(['Rifa']) : menambahkan data secara iterable
#
#    nama.append -> ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', [‘Rifa’, ‘Andi’, ‘Budi’]]
#    nama.extend ->  ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', ‘Rifa’, ‘Andi’, ‘Budi’]

# Jawaban yang benar adalah: b. nama.pop('Rifa') dan d. nama.insert('Rifa')
#
# Penjelasan
# Mari kita bahas setiap opsi satu per satu dan mengapa opsi b dan d
# tidak dapat digunakan untuk menambahkan 'Rifa' ke dalam list.
#
# a. nama.append('Rifa'):
# Fungsi: append menambahkan satu elemen baru di akhir list.
# Output: List akan menjadi ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', 'Rifa'].
# Penjelasan: Ini adalah cara yang benar untuk menambahkan 'Rifa' di posisi akhir list.
#
# b. nama.pop('Rifa'):
# Fungsi: pop menghapus item di list berdasarkan indeks (bukan berdasarkan nilai item).
# Output: Akan menyebabkan error karena pop hanya menerima indeks sebagai parameter, bukan nilai.
# Penjelasan: pop tidak dapat digunakan untuk menambahkan item ke dalam list; malah,
# pop digunakan untuk menghapus item berdasarkan indeks. Oleh karena itu,
# nama.pop('Rifa') tidak valid untuk menambahkan 'Rifa'.
#
# c. nama.insert(1, 'Rifa'):
# Fungsi: insert menambahkan elemen baru pada indeks tertentu di list.
# Output: List akan menjadi ['Achmad', 'Rifa', 'Bowo', 'Rifqi', 'Riyan', 'Huda'].
# Penjelasan: Ini adalah cara yang benar untuk menambahkan 'Rifa' pada indeks tertentu dalam list.
#
# d. nama.insert('Rifa'):
# Fungsi: insert memerlukan dua argumen: indeks tempat elemen akan ditambahkan dan elemen itu sendiri.
# Output: Akan menyebabkan error karena insert membutuhkan indeks yang didefinisikan.
# Penjelasan: insert memerlukan dua parameter, dan jika hanya diberikan satu (misalnya, 'Rifa'),
# Python akan menimbulkan error. Oleh karena itu, nama.insert('Rifa') tidak valid untuk menambahkan 'Rifa'.
#
# e. nama.extend(['Rifa']):
# Fungsi: extend menambahkan setiap elemen dari iterable (seperti list) ke list asli.
# Output: List akan menjadi ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', 'Rifa'].
# Penjelasan: extend akan menambahkan 'Rifa' sebagai elemen baru di akhir list,
# sehingga ini adalah cara yang benar untuk menambahkan 'Rifa'.
#
# Kesimpulan
# Opsi yang tidak dapat digunakan untuk menambahkan 'Rifa' ke dalam list adalah:
#
# b. nama.pop('Rifa') — karena pop digunakan untuk menghapus item berdasarkan indeks, bukan menambahkan item.
# d. nama.insert('Rifa') — karena insert memerlukan dua argumen: indeks dan elemen yang akan ditambahkan.
# Tambahan Penjelasan Mengenai append dan extend
# nama.append(['Rifa', 'Andi', 'Budi']) akan menambahkan list tersebut sebagai satu elemen tunggal di akhir list,
# sehingga hasilnya adalah ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', ['Rifa', 'Andi', 'Budi']].
# nama.extend(['Rifa', 'Andi', 'Budi']) akan menambahkan setiap elemen
# dalam list tersebut sebagai elemen individu di list asli,
# sehingga hasilnya adalah ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda', 'Rifa', 'Andi', 'Budi'].

# =============================================================================================
# Soal 6
# 6. Diantara tipe data berikut, manakah yang bukan termasuk pada collection data types?
#    a. Set
#    b. Tuple
#    c. List
#    d. Dictionary
#    e. Float  --> Jawaban
#
# Jawaban
# Jawaban yang benar adalah: e. Float
#
# Penjelasan
# Di dalam Python, collection data types adalah tipe data yang dapat digunakan
# untuk menyimpan beberapa item atau kumpulan data. Tipe data ini memungkinkan penyimpanan data yang terdiri
# dari banyak elemen di dalam satu variabel. Beberapa collection data types yang umum di Python meliputi:
#
# Set: Digunakan untuk menyimpan kumpulan elemen unik yang tidak berurutan.
# Contoh: my_set = {1, 2, 3}
#
# Tuple: Digunakan untuk menyimpan urutan elemen yang tidak dapat diubah (immutable).
# Contoh: my_tuple = (1, 2, 3)
#
# List: Digunakan untuk menyimpan urutan elemen yang dapat diubah (mutable).
# Contoh: my_list = [1, 2, 3]
#
# Dictionary: Digunakan untuk menyimpan pasangan kunci-nilai (key-value pairs), di mana setiap nilai diakses melalui kunci uniknya.
# Contoh: my_dict = {'key1': 'value1', 'key2': 'value2'}
#
# Kelima tipe data di atas (Set, Tuple, List, dan Dictionary) adalah tipe data koleksi (collection data types)
# karena mereka menyimpan kumpulan data yang berisi beberapa elemen.
#
# Penjelasan tentang Float
# Float adalah tipe data numerik yang digunakan untuk menyimpan bilangan desimal.
#
# Contoh: my_float = 3.14
# Float bukan tipe data koleksi, karena hanya menyimpan satu nilai numerik,
# bukan kumpulan atau koleksi dari beberapa nilai.
# Kesimpulan
# Oleh karena itu, jawaban yang benar adalah e. Float, karena float bukan termasuk
# tipe data koleksi (collection data types).

# =============================================================================================
# Soal 7
# 7. Jika terdapat kalimat:
#    nama = 'Saya Adalah Rifa Fitrianti'
#    Maka ketika Anda mengakses nama[4], output yang dikeluarkan adalah
#    a. 'S' : 0
#    b. 'a' : 1
#    c. 'y' : 2
#    d. ' ' : 4 --> Jawaban
#    e. 'A': 5
#
# Jawaban yang benar adalah: d. ' ' : 4
#
# Penjelasan
# Di Python, string merupakan urutan karakter yang dapat diakses menggunakan indeks.
# Indeks dimulai dari 0 untuk karakter pertama, 1 untuk karakter kedua, dan seterusnya.
#
# Untuk string nama = 'Saya Adalah Rifa Fitrianti', mari kita lihat indeks masing-masing karakter di dalam string:
#
# Indeks	Karakter
# 0	'S'
# 1	'a'
# 2	'y'
# 3	'a'
# 4	' ' (spasi)
# 5	'A'
# 6	'd'
# 7	'a'
# 8	'l'
# 9	'a'
# 10	'h'
# 11	' ' (spasi)
# 12	'R'
# 13	'i'
# 14	'f'
# 15	'a'
# 16	' ' (spasi)
# 17	'F'
# 18	'i'
# 19	't'
# 20	'r'
# 21	'i'
# 22	'a'
# 23	'n'
# 24	't'
# 25	'i'
# Ketika kita mengakses nama[4], kita mendapatkan karakter pada indeks ke-4, yang merupakan spasi (' ').
#
# Kesimpulan
# Jawaban yang benar adalah d. ' ' : 4, karena karakter pada indeks 4 adalah spasi (' ').
#
# Alasan Pilihan Lainnya Salah
# a. 'S' : 0 — 'S' berada di indeks 0, bukan 4.
# b. 'a' : 1 — 'a' pertama berada di indeks 1, bukan 4.
# c. 'y' : 2 — 'y' berada di indeks 2, bukan 4.
# e. 'A': 5 — 'A' berada di indeks 5, bukan 4.

# =============================================================================================
# Soal 8
# 8. nama = ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda']
#    Maka untuk menghapus karakter value terakhir pada list menggunakan perintah . . . .
#    delete nama('Huda') : del nama(‘Huda’)
#    a. nama.clear() : [ ]
#    b. nama.capitalize() : []
#    c. nama.append()
#    d. nama.pop() : menghapus data pada value terakhir --> Jawaban
#
# Jawaban
# Jawaban yang benar adalah: e. nama.pop() : menghapus data pada value terakhir
#
# Penjelasan
# Di Python, untuk menghapus elemen terakhir dalam sebuah list, kita bisa menggunakan metode .pop().
# Metode ini akan menghapus dan mengembalikan item terakhir dalam list.
# Jika tidak ada indeks yang diberikan, .pop() akan secara otomatis menghapus elemen terakhir dari list.
#
# Untuk list nama = ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda'], menggunakan nama.pop() akan menghapus 'Huda',
# yang merupakan elemen terakhir.
#
# Script Python
#
# nama = ['Achmad', 'Bowo', 'Rifqi', 'Riyan', 'Huda']
# nama.pop()  # Menghapus elemen terakhir
# print(nama)
#
# Output
#
# ['Achmad', 'Bowo', 'Rifqi', 'Riyan']
# Alasan Pilihan Lainnya Salah
#
# a. delete nama('Huda') : del nama('Huda')
# Salah karena del digunakan untuk menghapus item dari list menggunakan indeks, bukan nilai langsung.
# Sintaks yang benar untuk menghapus 'Huda' (dengan mengetahui indeksnya) akan berupa del nama[4].
#
# b. nama.clear() : []
# Salah karena clear() menghapus semua elemen dalam list, sehingga list akan menjadi kosong ([]).
# Ini bukan cara yang tepat untuk hanya menghapus elemen terakhir.
#
# c. nama.capitalize() : []
# Salah karena capitalize() adalah metode string, bukan metode list. Ini tidak dapat digunakan untuk
# menghapus elemen dalam list.
#
# d. nama.append()
# Salah karena append() digunakan untuk menambahkan elemen ke list, bukan untuk menghapusnya.
#
# e. nama.pop()
# Benar karena pop() menghapus elemen terakhir dalam list, yang sesuai dengan soal.
#
# Kesimpulan
# Jawaban yang benar adalah e. nama.pop() karena
# .pop() adalah metode yang tepat untuk menghapus elemen terakhir dalam list di Python.

# =============================================================================================
# Soal 9
# 9. Yang mana pernyataan tentang list berikut ini yang benar?
#    a. list dapat diubah nilainya : mutable --> Jawaban
#    b. value list harus homogen (memiliki tipe data yang semua sama) : bisa heterogen
#    c. value list tidak boleh duplikat : duplicate
#    d. list tidak dapat diubah nilainya : dapat diubah
#    e. terdapat key dan value pada list : dictionary
#
# Jawaban
# Jawaban yang benar adalah: a. list dapat diubah nilainya : mutable
#
# Penjelasan
# Di Python, list adalah struktur data yang mendukung perubahan nilai-nilai di dalamnya, yang disebut mutable.
# List juga memiliki karakteristik khusus lainnya, yang membedakannya dari struktur data lain
# seperti tuple atau dictionary. Berikut penjelasan untuk setiap opsi:
#
# a. list dapat diubah nilainya : mutable
# Benar. List di Python bersifat mutable, artinya nilai-nilai di dalam list dapat diubah setelah list dibuat.
# Kita bisa menambah, menghapus, atau memodifikasi elemen dalam list sesuai kebutuhan.
#
# Contoh:
# my_list = [1, 2, 3]
# my_list[1] = 10  # Mengubah elemen kedua
# print(my_list)  # Output: [1, 10, 3]
#
# b. value list harus homogen (memiliki tipe data yang semua sama) : bisa heterogen
# Salah. List di Python tidak harus memiliki elemen dengan tipe data yang sama; list dapat bersifat heterogen. Ini berarti kita bisa memiliki elemen dengan tipe data berbeda dalam satu list.
# Contoh:
#
# my_list = [1, "hello", 3.14]  # Integer, string, dan float dalam satu list
#
# c. value list tidak boleh duplikat : duplicate
# Salah. List di Python boleh mengandung elemen duplikat. Tidak ada batasan untuk memiliki elemen
# yang sama berkali-kali dalam list.
# Contoh:
# my_list = [1, 2, 2, 3, 3, 3]  # List dengan elemen duplikat
#
# d. list tidak dapat diubah nilainya : dapat diubah
# Salah. List bersifat mutable sehingga nilai-nilai di dalamnya dapat diubah. Pernyataan ini lebih cocok
# untuk tipe data tuple, yang bersifat immutable.
#
# e. terdapat key dan value pada list : dictionary
# Salah. Hanya dictionary yang memiliki konsep key-value pairs. List di Python hanya memiliki elemen-elemen
# yang diakses berdasarkan indeks, bukan berdasarkan kunci.
#
# Kesimpulan
# Jawaban yang benar adalah a. list dapat diubah nilainya : mutable, karena list di Python bersifat mutable dan dapat diubah setelah didefinisikan.
# Opsi lainnya salah karena:
#
# List bisa berisi tipe data yang berbeda (heterogen).
# List dapat mengandung elemen duplikat.
# List dapat diubah nilainya.
# List tidak memiliki key-value pairs; konsep ini hanya ada pada dictionary.

# =============================================================================================
# Soal 10
# 10. Output yang benar adalah ...
#     x = 50 / 10
#     print(type(x))
#     a. int
#     b. float --> Jawaban
#     c. str
#     d. bool
#
# Jawaban
# Jawaban yang benar adalah: b. float
#
# Penjelasan
# Di Python, operator pembagian / selalu menghasilkan nilai dengan tipe data float, meskipun hasil pembagiannya
# merupakan bilangan bulat. Hal ini berlaku baik pada Python 2 maupun Python 3.
#
# Pada script dibawah ini :
#
# x = 50 / 10
# print(type(x))
#
# 50 / 10: Operasi ini menghasilkan nilai 5.0.
# type(x): Fungsi type() digunakan untuk mengetahui tipe data dari variabel x. Karena 50 / 10 menghasilkan 5.0 (float),
# maka type(x) akan mengembalikan <class 'float'>.
#
# Penjelasan Opsi Lainnya :
# * a. int : Salah, karena operator / selalu menghasilkan tipe float, meskipun hasil pembagiannya berupa bilangan bulat.
# * c. str : Salah, karena x adalah hasil operasi aritmatika dan buka tipe string.
# * d. bool : Salah, karena tipe data boolean hanya memiliki nilai True atau False, bukan hasil pembagian.
#
# Jadi, jawaban yang benar adalah b. float
# =============================================================================================
# Soal 11
# 11. Pilih kode yang menghasilkan output 3.14.
#     a. print(math.floor(math.pi))
#     b. print(round((math.pi)))
#     c. print(round((math.pi), 2)) --> Jawaban
#     d. print(22 / 7)
#
# Jawaban
# Jawaban yang benar adalah: c. print(round((math.pi), 2))
#
# Penjelasan
# Mari kita analisis setiap opsi untuk melihat mana yang akan menghasilkan output 3.14:
#
# a. print(math.floor(math.pi)):
# Penjelasan: math.floor() mengembalikan nilai terbesar yang kurang dari atau sama dengan argumen yang diberikan.
# Dalam kasus math.pi (yang nilainya sekitar 3.14159), math.floor(math.pi) akan menghasilkan 3, bukan 3.14.
# Output: 3
# Kesimpulan: Salah, karena hasilnya bukan 3.14.
#
# b. print(round((math.pi))):
# Penjelasan: round() dengan satu argumen akan membulatkan angka ke bilangan bulat terdekat.
# Jadi, round(math.pi) akan membulatkan 3.14159 ke 3, bukan 3.14.
# Output: 3
# Kesimpulan: Salah, karena hasilnya bukan 3.14.
#
# c. print(round((math.pi), 2)):
# Penjelasan: round() dengan dua argumen, di mana argumen kedua menunjukkan jumlah desimal yang diinginkan.
# Dalam hal ini, round(math.pi, 2) akan membulatkan math.pi hingga dua tempat desimal, yang menghasilkan 3.14.
# Output: 3.14
# Kesimpulan: Benar, karena ini menghasilkan output 3.14.
#
# d. print(22 / 7):
# Penjelasan: 22 / 7 adalah perkiraan untuk pi, tetapi nilainya tidak persis sama dengan pi.
# Hasil dari 22 / 7 adalah sekitar 3.142857, bukan 3.14.
# Output: 3.142857142857143
#
# Kesimpulan: Salah, karena hasilnya bukan 3.14.
#
# Kesimpulan
# Jawaban yang benar adalah c. print(round((math.pi), 2))
# karena perintah ini akan membulatkan nilai math.pi ke dua tempat desimal, menghasilkan output 3.14.
# Opsi lainnya salah karena:
#
# a menghasilkan 3.
# b juga menghasilkan 3.
# d menghasilkan sekitar 3.142857, bukan 3.14.
# =============================================================================================
# Soal 12
# 12. Terdapat code sebagai berikut :
#       a = 100
#       b = 200
#
#       a = b
#
#       print(a)
#
#       Output yang benar adalah :
#       a. 100
#       b. 200  --> Jawaban
#       c. False
#       d. TypeError
#
# Jawaban
# Jawaban yang benar adalah: b. 200
#
# Penjelasan
# Mari kita analisis kode berikut:
#
# a = 100
# b = 200
#
# a = b
#
# print(a)
#
# a = 100: Variabel a diberi nilai 100.
# b = 200: Variabel b diberi nilai 200.
#
# a = b: Pada baris ini, kita menetapkan nilai variabel b (yang adalah 200) ke variabel a.
# Jadi, sekarang a memiliki nilai 200.
# print(a): Ketika kita mencetak a, hasilnya adalah 200, karena nilai a telah diubah menjadi nilai b.
#
# Kesimpulan
# Output yang benar adalah 200.
#
# Alasan Pilihan Lainnya Salah
#
# a. 100: Salah, karena setelah a = b, nilai a diubah menjadi 200.
#
# c. False: Salah, karena tidak ada operasi boolean yang menghasilkan nilai False.
#
# d. TypeError: Salah, karena tidak ada error tipe dalam kode ini; semua operasi valid.
# Jadi, jawaban yang benar adalah b. 200.

# =============================================================================================
# Soal 13
# 13. Terdapat code sebagai berikut :
# bayar = input('Masukkan nominal 0 - 10 :')
# harga_barang = 7
#
# if bayar > harga_barang:
#     print('Terima kasih')
# else:
#     print('Uang Anda tidak cukup')
#
#   Ketika muncul 'Masukkan nominal 0 - 10 :' di terminal dan kita ketik 9, maka output yang muncul adalah
#   a. Terima kasih
#   b. Uang Anda tidak cukup
#   c. TypeError  --> Jawaban
#   d. 9
#
# Jawaban
# Jawaban yang benar adalah: c. TypeError
#
# Penjelasan
# Mari kita analisis kode berikut:
#
# python
# Salin kode
# bayar = input('Masukkan nominal 0 - 10 :')
# harga_barang = 7
#
# if bayar > harga_barang:
#     print('Terima kasih')
# else:
#     print('Uang Anda tidak cukup')
# input(): Fungsi input() di Python selalu mengembalikan nilai dalam bentuk string.
# Jadi, ketika kita memasukkan nilai 9, variabel bayar akan berisi string '9', bukan integer 9.
#
# if bayar > harga_barang: Di sini, kita mencoba membandingkan bayar (yang bertipe string)
# dengan harga_barang (yang bertipe integer). Python tidak mengizinkan perbandingan langsung antara string dan integer,
# sehingga akan menghasilkan TypeError.
#
# Error yang Muncul: Karena Python tidak bisa membandingkan string dengan integer, maka kode ini akan menimbulkan error:
#
# TypeError: '>' not supported between instances of 'str' and 'int'
#
# Cara Memperbaiki
# Untuk memperbaiki kode ini, kita perlu mengonversi input dari bayar ke integer agar bisa dibandingkan
# dengan harga_barang:
#
# bayar = int(input('Masukkan nominal 0 - 10 :'))
# harga_barang = 7
#
# if bayar > harga_barang:
#     print('Terima kasih')
# else:
#     print('Uang Anda tidak cukup')
# Dengan kode ini, jika kita memasukkan 9, maka outputnya akan menjadi:
#
# Kesimpulan
# Jawaban yang benar adalah c. TypeError karena terjadi kesalahan saat mencoba membandingkan string dengan integer.

# =============================================================================================
# Soal 14
# 14. Terdapat code sebagai berikut :
#      kalimat = 'Selamat datang di Indonesia'
#      print(kalimat[1:-1])
#
#      Output yang benar adalah
#         a. Selamat datang di Indonesia
#         b. Selamat datang di Indonesi
#         c. elamat datang di Indonesia
#         d. elamat datang di Indonesi --> Jawaban
#
# Jawaban
# Jawaban yang benar adalah: d. elamat datang di Indonesi
#
# Penjelasan
# Mari kita analisis kode berikut:
#
# kalimat = 'Selamat datang di Indonesia'
# print(kalimat[1:-1])
#
# 1. String Slicing: Dalam Python, kita bisa menggunakan slicing dengan sintaks string[start:end]
# untuk mengambil bagian tertentu dari sebuah string. start adalah indeks awal (termasuk),
# dan end adalah indeks akhir (tidak termasuk).
#
# 2. Indeks 1:-1:
# kalimat[1:-1] berarti kita mengambil karakter dari indeks 1 hingga -1.
# Indeks 1 merujuk pada karakter kedua dalam string, yaitu 'e'.
# Indeks -1 berarti karakter terakhir dari string (dalam hal ini, 'a'), tetapi karena slicing
# di Python tidak menyertakan indeks akhir, karakter terakhir 'a' tidak akan termasuk dalam hasil.
#
# 3. Hasil Slicing:
# String kalimat[1:-1] akan berisi semua karakter dari indeks 1 hingga sebelum indeks terakhir,
# menghasilkan 'elamat datang di Indonesi'.
#
# Kesimpulan
# Jawaban yang benar adalah d. elamat datang di Indonesi karena slicing kalimat[1:-1]
# akan menghilangkan karakter pertama 'S' dan karakter terakhir 'a', menghasilkan 'elamat datang di Indonesi'.
#
# Alasan Pilihan Lainnya Salah
# a. Selamat datang di Indonesia — salah, karena ini adalah string asli tanpa slicing.
#
# b. Selamat datang di Indonesi — salah, karena slicing kalimat[1:-1] tidak menyertakan huruf pertama 'S'.
#
# c. elamat datang di Indonesia — salah, karena slicing kalimat[1:-1] menghilangkan karakter terakhir 'a'.

# =============================================================================================
# Soal 15
# 15. Terdapat code sebagi berikut :
#       kota = ['Jakarta', 'Bandung', 'Surabaya']
#
#       print([i.thisFunction() for i in kota])
#
#       Agar output yang dihasilkan adalah ['jakarta','bandung','surabaya'], maka function yang tepat untuk menggantikan
#       thisFunction()
#       a. upper()
#       b. capitalize()
#       c. lower()  --> Jawaban
#       d. isLower()
# Jawaban
# Jawaban yang benar adalah: c. lower()
#
# Penjelasan
# Kode berikut menggunakan list comprehension untuk menerapkan fungsi tertentu pada setiap elemen di dalam list kota:
#
# python
# Salin kode
# kota = ['Jakarta', 'Bandung', 'Surabaya']
# print([i.thisFunction() for i in kota])
# Tujuan dari soal ini adalah untuk mengubah setiap nama kota menjadi huruf kecil,
# sehingga output yang dihasilkan adalah ['jakarta', 'bandung', 'surabaya'].
#
# Mari kita analisis setiap opsi:
#
# a. upper():
# Penjelasan: upper() mengubah semua huruf dalam string menjadi huruf kapital.
# Output jika digunakan: ['JAKARTA', 'BANDUNG', 'SURABAYA'].
# Kesimpulan: Salah, karena kita menginginkan hasil dalam huruf kecil, bukan huruf kapital.
#
# b. capitalize():
# Penjelasan: capitalize() hanya mengubah huruf pertama dari string menjadi huruf kapital, dan
# semua huruf lainnya menjadi huruf kecil.
# Output jika digunakan: ['Jakarta', 'Bandung', 'Surabaya'] (tidak ada perubahan dalam list ini
# karena elemen-elemen sudah dalam format yang diinginkan oleh capitalize()).
# Kesimpulan: Salah, karena kita menginginkan semua huruf dalam bentuk huruf kecil.
#
# c. lower():
# Penjelasan: lower() mengubah semua huruf dalam string menjadi huruf kecil.
# Output jika digunakan: ['jakarta', 'bandung', 'surabaya'].
# Kesimpulan: Benar, karena ini menghasilkan output yang sesuai dengan soal, yaitu semua huruf dalam bentuk huruf kecil.
#
# d. isLower():
# Penjelasan: isLower() adalah metode yang mengembalikan True jika semua huruf dalam string sudah dalam huruf kecil.
# Metode ini tidak mengubah string, hanya memeriksa apakah string tersebut dalam huruf kecil atau tidak.
# Output jika digunakan: Akan menghasilkan error karena isLower() tidak mengubah string,
# sehingga tidak sesuai dengan kebutuhan soal.
#
# Kesimpulan: Salah, karena isLower() tidak mengubah string menjadi huruf kecil.
# Kesimpulan
# Jawaban yang benar adalah c. lower() karena fungsi ini akan mengubah semua huruf dalam string menjadi huruf kecil,
# sesuai dengan output yang diinginkan: ['jakarta', 'bandung', 'surabaya'].

# =============================================================================================
# Soal 16
16. Terdapat code sebagai berikut :
listAngka = []

for i in range(2, 22, 2):
    if i == 8:
        continue
    elif i == 14:
        break
    else:
        listAngka.append(i)

print(listAngka)

Output yang benar adalah
a. [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
b. [2, 4, 6, 8, 10, 12]
c. [2, 4, 6, 10, 12] --> Jawaban
d. [2, 4, 6, 8]

Jawaban
Jawaban yang benar adalah: c. [2, 4, 6, 10, 12]

Penjelasan
Mari kita analisis kode berikut:

listAngka = []

for i in range(2, 22, 2):
    if i == 8:
        continue
    elif i == 14:
        break
    else:
        listAngka.append(i)

print(listAngka)
Penjelasan Kode

1. range(2, 22, 2):
range(2, 22, 2) menghasilkan bilangan genap dari 2 hingga 20 (karena 22 tidak termasuk).
Angka-angka yang dihasilkan adalah: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

2. Loop dan Kondisi:
Ketika i == 8: continue akan dijalankan, sehingga loop langsung melanjutkan ke iterasi berikutnya, dan
8 tidak akan ditambahkan ke listAngka.
Ketika i == 14: break akan dijalankan, sehingga loop akan berhenti sepenuhnya, dan
angka 14 serta semua angka setelahnya tidak akan ditambahkan ke listAngka.
Lainnya: Jika i tidak sama dengan 8 atau 14, maka nilai i akan ditambahkan ke listAngka.

3. Iterasi dan Hasil:
Iterasi pertama: i = 2 → ditambahkan ke listAngka.
Iterasi kedua: i = 4 → ditambahkan ke listAngka.
Iterasi ketiga: i = 6 → ditambahkan ke listAngka.
Iterasi keempat: i = 8 → continue (dilewati).
Iterasi kelima: i = 10 → ditambahkan ke listAngka.
Iterasi keenam: i = 12 → ditambahkan ke listAngka.
Iterasi ketujuh: i = 14 → break (loop berhenti).

4. Output:
Setelah loop selesai, listAngka berisi [2, 4, 6, 10, 12].

Kesimpulan
Jawaban yang benar adalah c. [2, 4, 6, 10, 12] karena angka 8 dilewati dengan continue, dan
angka 14 menyebabkan loop berhenti dengan break.
# =============================================================================================
# Soal 17
17. Terdapat code sebagai berikut :
    ibuKota = {
        'Jepang' : 'Tokyo',
        'Jerman' : 'Dortmund',
        'Inggris' : London
    }
Code yang tepat untuk mengubah value yang dimiliki 'Jerman' dari 'Dortmund' menjadi 'Berlin' adalah
a. ibuKota.replace({'Jerman' : 'Berlin'})
b. ibuKota['Jerman'] : 'Berlin'
c. ibuKota['Jerman'] = 'Berlin' --> Jawaban
d. ibuKota.value{'Jerman' : 'Berlin'}

Jawaban
Jawaban yang benar adalah: c. ibuKota['Jerman'] = 'Berlin'

Penjelasan
Di Python, dictionary adalah struktur data yang berisi pasangan key-value. Untuk mengubah nilai (value)
yang terkait dengan kunci (key) tertentu, kita bisa mengakses key tersebut dan menetapkan nilai baru
dengan sintaks dictionary[key] = new_value.

Mari kita analisis setiap opsi dan mengapa hanya opsi c yang benar:

a. ibuKota.replace({'Jerman' : 'Berlin'}):
Penjelasan: replace() adalah metode yang digunakan untuk string, bukan dictionary. Dictionary di Python
tidak memiliki metode replace().
Kesimpulan: Salah, karena replace() tidak berlaku untuk dictionary.

b. ibuKota['Jerman'] : 'Berlin':
Penjelasan: Ini adalah sintaks yang salah. : digunakan untuk menetapkan pasangan key-value
saat mendefinisikan dictionary, bukan saat mengubah nilai di dictionary. Untuk mengubah nilai, seharusnya menggunakan =.
Kesimpulan: Salah, karena menggunakan : alih-alih = untuk mengubah nilai.

c. ibuKota['Jerman'] = 'Berlin':
Penjelasan: Ini adalah cara yang benar untuk mengubah nilai dalam dictionary.
Dengan menuliskan ibuKota['Jerman'] = 'Berlin', kita mengakses key 'Jerman' dan
menetapkan nilai baru 'Berlin' untuk key tersebut.
Kesimpulan: Benar, karena ini adalah cara yang tepat untuk mengubah nilai dari 'Dortmund' menjadi 'Berlin'.

d. ibuKota.value{'Jerman' : 'Berlin'}:
Penjelasan: Ini juga merupakan sintaks yang salah. value bukan metode yang ada pada dictionary, dan {}
hanya digunakan untuk membuat dictionary baru atau dalam pengaksesan key-value.

Kesimpulan: Salah, karena value tidak ada dalam konteks pengubahan nilai di dictionary.
Kesimpulan
Jawaban yang benar adalah c. ibuKota['Jerman'] = 'Berlin' karena ini adalah cara yang benar
untuk mengubah nilai dalam dictionary di Python.

Contoh Kode Lengkap
Berikut adalah kode yang tepat untuk mengubah nilai dalam dictionary:

ibuKota = {
    'Jepang' : 'Tokyo',
    'Jerman' : 'Dortmund',
    'Inggris' : 'London'
}

# Mengubah nilai dari 'Jerman' menjadi 'Berlin'
ibuKota['Jerman'] = 'Berlin'

print(ibuKota)

# =============================================================================================
# Soal 18
# 18. Terdapat code sebagai berikut :
#     car = ['Honda', 'BMW', 'TESLA']
#     manufacturer = ['Japan', 'Germany', 'USA']
#
#     for i in something:
#         print(f'{car[i]} is from {manufacturer[i]}')
#
# Output yang diharapkan: Honda is from Japan BMW is from Germany Tesla is from USA.
# Code yang benar untuk menggantikan something adalah
# a. car
# b. manufacturer
# c. range(len(car)) --> Jawaban
# d. range(0,2)
#
# Jawaban
# Jawaban yang benar adalah: c. range(len(car))
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# car = ['Honda', 'BMW', 'TESLA']
# manufacturer = ['Japan', 'Germany', 'USA']
#
# for i in something:
#     print(f'{car[i]} is from {manufacturer[i]}')
#
# Dalam kode di atas, kita ingin mengakses elemen di list car dan manufacturer berdasarkan indeksnya
# sehingga kita dapat mencetak kombinasi merek mobil dengan negaranya. Untuk itu, kita perlu mengganti something
# dengan sesuatu yang akan menghasilkan indeks dari elemen-elemen dalam list tersebut.
#
# Penjelasan untuk Setiap Opsi
#
# a. car:
# Penjelasan: Jika kita menggunakan car sebagai something, maka i akan menjadi elemen dari list car,
# yaitu 'Honda', 'BMW', dan 'TESLA', bukan indeks.
# Kesimpulan: Salah, karena kita membutuhkan indeks (bukan elemen list)
# untuk mengakses elemen yang sesuai di kedua list (car dan manufacturer).
#
# b. manufacturer:
# Penjelasan: Sama seperti opsi car, jika kita menggunakan manufacturer sebagai something,
# maka i akan menjadi elemen dari list manufacturer, yaitu 'Japan', 'Germany', dan 'USA', bukan indeks.
# Kesimpulan: Salah, karena kita membutuhkan indeks untuk mengakses elemen yang sesuai di kedua list.
#
# c. range(len(car)):
# Penjelasan: range(len(car)) menghasilkan urutan indeks yang sesuai dengan panjang list car, yaitu range(3),
# yang setara dengan [0, 1, 2]. Dengan ini, i akan menjadi indeks 0, 1, dan 2 pada setiap iterasi,
# sehingga kita bisa mengakses car[i] dan manufacturer[i] untuk setiap elemen.
# Kesimpulan: Benar, karena ini menghasilkan indeks yang sesuai dengan panjang list
# dan memungkinkan kita mencetak kombinasi car[i] dan manufacturer[i].
#
# d. range(0, 2):
# Penjelasan: range(0, 2) menghasilkan urutan [0, 1], yang hanya akan mengakses dua elemen pertama dari setiap list.
# Ini akan melewatkan elemen terakhir (TESLA dan USA).
#
# Kesimpulan: Salah, karena tidak mencakup seluruh indeks dari list.
#
# Kesimpulan
# Jawaban yang benar adalah c. range(len(car)) karena ini menghasilkan indeks yang sesuai dengan panjang list car
# dan manufacturer, memungkinkan kita untuk mengakses setiap elemen dalam kedua list dan mencetak output yang diharapkan.

# =============================================================================================
# Soal 19
# 19. Terdapat code sebagi berikut :
#     day = ['Monday', 'Wednesday', 'Friday']
#
#     weekend = ['Saturday', 'Sunday']
#
#     day.myFunction(weekend)
#
#     print(day)
#
# Output: ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']. Function yang tepat
# untuk menggantikan myFunction adalah
# a. add
# b. append : [ [‘Saturday’, ‘Sunday’]]
# c. extend : ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'] --> Jawaban
# d. insert
#
# Jawaban
# Jawaban yang benar adalah: c. extend : ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# day = ['Monday', 'Wednesday', 'Friday']
# weekend = ['Saturday', 'Sunday']
#
# day.myFunction(weekend)
# print(day)
#
# Tujuan dari kode ini adalah untuk menambahkan elemen-elemen dari list weekend ke dalam list day,
# sehingga hasil akhirnya adalah ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'].
#
# Penjelasan untuk Setiap Opsi
# a. add:
# Penjelasan: add bukan metode yang valid untuk list di Python. add digunakan
# untuk menambahkan elemen pada set, bukan list.
# Kesimpulan: Salah, karena add tidak berlaku untuk list.
#
# b. append:
# Penjelasan: append menambahkan satu elemen ke akhir list. Jika kita menggunakan append(weekend),
# maka keseluruhan list weekend akan ditambahkan sebagai satu elemen tunggal,
# menghasilkan list yang berisi sublist [['Saturday', 'Sunday']] di akhir.
# Output jika digunakan: ['Monday', 'Wednesday', 'Friday', ['Saturday', 'Sunday']]
# Kesimpulan: Salah, karena hasilnya akan menambahkan weekend sebagai sublist, bukan sebagai elemen individu.
#
# c. extend:
# Penjelasan: extend menambahkan setiap elemen dari iterable (dalam hal ini, weekend) secara individual ke akhir list day.
# Dengan menggunakan extend, elemen 'Saturday' dan 'Sunday' dari list weekend
# akan ditambahkan ke day sebagai elemen individu, bukan sebagai sublist.
# Output jika digunakan: ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
# Kesimpulan: Benar, karena extend adalah fungsi yang tepat untuk menggabungkan kedua list
# dengan menambahkan setiap elemen dari weekend ke day.
#
# d. insert:
# Penjelasan: insert digunakan untuk menambahkan satu elemen pada posisi tertentu dalam list.
# Ini bukan cara yang tepat untuk menambahkan seluruh elemen dari list weekend ke day
# tanpa menentukan posisi untuk setiap elemen.
#
# Kesimpulan: Salah, karena insert hanya menambahkan satu elemen pada indeks tertentu, bukan semua elemen dari weekend.
# Kesimpulan
# Jawaban yang benar adalah c. extend karena extend menambahkan setiap elemen dari list weekend ke list day
# sebagai elemen individu, menghasilkan output yang diharapkan: ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'].

# =============================================================================================
# Soal 20
20. pet = ['cat', 'dog', 'rabbit', 'turtle']

Method apa yang digunakan untuk mengetahui index dari 'dog'

a. pet.index('dog') --> Jawaban
b. pet.search('dog')
c. pet.find('dog')
d. pet.where('dog')

Jawaban
Jawaban yang benar adalah: a. pet.index('dog')

Penjelasan
Dalam Python, untuk menemukan indeks dari suatu elemen di dalam list, kita bisa menggunakan metode .index().
Metode ini mengembalikan indeks pertama kali kemunculan elemen yang dicari.
Jika elemen tersebut tidak ada dalam list, maka akan menghasilkan ValueError.

Mari kita analisis setiap opsi:

a. pet.index('dog'):
Penjelasan: index() adalah metode yang benar untuk menemukan indeks dari elemen 'dog' di dalam list pet.
Ini akan mengembalikan indeks elemen 'dog' di dalam list.
Output jika digunakan: 1, karena 'dog' berada pada indeks 1 di list pet.
Kesimpulan: Benar, karena ini adalah cara yang tepat untuk mengetahui indeks dari elemen 'dog'.

b. pet.search('dog'):
Penjelasan: search() bukan metode yang valid untuk list di Python. Metode search() tidak ada untuk list.
Kesimpulan: Salah, karena search() tidak berlaku untuk list.

c. pet.find('dog'):
Penjelasan: find() adalah metode yang digunakan untuk string dalam Python, bukan untuk list.
Metode find() mengembalikan indeks kemunculan pertama dari substring dalam string, tetapi tidak ada untuk list.
Kesimpulan: Salah, karena find() tidak berlaku untuk list.

d. pet.where('dog'):
Penjelasan: where() juga bukan metode yang valid untuk list di Python. Tidak ada metode where() dalam list.

Kesimpulan: Salah, karena where() tidak berlaku untuk list.
Kesimpulan
Jawaban yang benar adalah a. pet.index('dog') karena metode .index() adalah cara yang tepat untuk menemukan indeks
dari suatu elemen dalam list di Python.

Contoh Kode
Berikut adalah kode yang benar untuk menemukan indeks dari 'dog' dalam list pet:

# =============================================================================================
# Soal 21
# 21. Terdapat code sebagai berikut :
#     plane = 'Boeing747'
#
# Method apa yang digunakan agar outputnya True
# a. print(plane.isdecimal()) : False
# b. print(plane.isalphanumeric()) : Tidak ada / error
# c. print(plane.isalnum()) : True --> Jawaban
# d. print(plane.isalpha()) : False
#
#
# awaban
# Jawaban yang benar adalah: c. print(plane.isalnum()) : True
#
# Penjelasan
# Mari kita analisis setiap opsi untuk memahami metode yang tepat agar outputnya True:
#
# Kode yang diberikan adalah:
#
# plane = 'Boeing747'
#
# String 'Boeing747' terdiri dari huruf (alfabet) dan angka,
# jadi metode yang mengembalikan True harus bisa mengenali kombinasi huruf dan angka.
#
# Penjelasan untuk Setiap Opsi
#
# a. print(plane.isdecimal()) : False
# Penjelasan: Metode isdecimal() mengembalikan True hanya jika semua karakter dalam string adalah angka desimal (0-9).
# Karena 'Boeing747' memiliki karakter alfabet selain angka, isdecimal() akan mengembalikan False.
# Output jika digunakan: False
# Kesimpulan: Salah, karena hasilnya adalah False.
#
# b. print(plane.isalphanumeric()) : Tidak ada / error
# Penjelasan: isalphanumeric() bukan metode yang valid dalam Python. Metode yang benar adalah isalnum().
# Jika kita mencoba menggunakan isalphanumeric(), Python akan menghasilkan error karena metode ini tidak ada.
# Kesimpulan: Salah, karena isalphanumeric() tidak ada dalam Python dan akan menyebabkan error.
#
# c. print(plane.isalnum()) : True
# Penjelasan: Metode isalnum() mengembalikan True jika semua karakter dalam string adalah huruf (alfabet) atau
# angka (0-9) tanpa spasi atau simbol. Karena 'Boeing747' hanya berisi huruf dan angka, isalnum() akan mengembalikan True.
# Output jika digunakan: True
# Kesimpulan: Benar, karena ini adalah metode yang tepat untuk memeriksa apakah string hanya berisi huruf dan angka.
#
# d. print(plane.isalpha()) : False
# Penjelasan: Metode isalpha() mengembalikan True hanya jika semua karakter dalam string adalah huruf (alfabet)
# dan tidak ada angka atau karakter lain. Karena 'Boeing747' mengandung angka, isalpha() akan mengembalikan False.
# Output jika digunakan: False
#
# Kesimpulan: Salah, karena hasilnya adalah False.
# Kesimpulan
# Jawaban yang benar adalah c. print(plane.isalnum()) : True karena metode isalnum() mengembalikan True
# untuk string yang hanya berisi huruf dan angka, yang sesuai dengan karakteristik string 'Boeing747'.
# Contoh Kode
# Berikut adalah kode yang benar untuk menghasilkan output True:
#
# plane = 'Boeing747'
# print(plane.isalnum())

# =============================================================================================
# Soal 22
# 22. Terdapat code sebagai berikut :
#     a = 'Selamat datang'
#
#     def katakan(nama):
#         a = ' Sampai jumpa'
#         print(f'{a} {nama}')
#
#     katakan ('Timo')
#
# Output yang benar adalah
#     a. Selamat datang Timo
#     b. Sampai jumpa Timo --> Jawaban
#     c. Timo Sampai jumpa
#     d. Selamat datang Sampai jumpa
#
# Jawaban
# Jawaban yang benar adalah: b. Sampai jumpa Timo
#
# Penjelasan
# Mari kita analisis kode berikut:
#
# a = 'Selamat datang'
#
# def katakan(nama):
#     a = 'Sampai jumpa'
#     print(f'{a} {nama}')
#
# katakan('Timo')
#
# Penjelasan Kode
#
# 1. Variabel Global a: Di luar fungsi katakan, kita mendefinisikan variabel a dengan nilai 'Selamat datang'.
# Ini adalah variabel global yang berada di luar cakupan fungsi katakan.
#
# 2. Variabel Lokal a di Dalam Fungsi:
#     * Di dalam fungsi katakan, kita mendefinisikan kembali variabel a dengan nilai 'Sampai jumpa'.
#
#     * Variabel a yang didefinisikan di dalam fungsi ini adalah variabel lokal
#     dan hanya berlaku di dalam cakupan fungsi katakan. Variabel ini
#     tidak mempengaruhi variabel global a yang berada di luar fungsi.
#
# 3. Pemanggilan Fungsi:
#     * Ketika katakan('Timo') dipanggil, fungsi katakan akan dijalankan dengan nama diisi dengan 'Timo'.
#     * Di dalam fungsi, Python akan menggunakan variabel lokal a = 'Sampai jumpa' (bukan variabel global a),
#       sehingga outputnya akan menjadi Sampai jumpa Timo.
#
# 4. Output:
#     * Fungsi print(f'{a} {nama}') akan mencetak 'Sampai jumpa Timo' karena a mengacu pada variabel lokal 'Sampai jumpa',
# dan nama berisi 'Timo'.
#
# Kesimpulan
# Jawaban yang benar adalah b. Sampai jumpa Timo karena variabel lokal a di dalam fungsi katakan
# menimpa variabel global a selama eksekusi fungsi.
#
# Alasan Pilihan Lainnya Salah
# a. Selamat datang Timo — Salah, karena variabel lokal a di dalam fungsi katakan berisi 'Sampai jumpa',
# bukan 'Selamat datang'.
#
# c. Timo Sampai jumpa — Salah, karena format output adalah f'{a} {nama}', sehingga a akan muncul sebelum nama.
#
# d. Selamat datang Sampai jumpa — Salah, karena variabel a dalam fungsi katakan hanya berisi 'Sampai jumpa',
# dan nama berisi 'Timo'.

# =============================================================================================
# Soal 23
# 23. Terdapat code sebagi berikut :
#     a, b, c = ["Banana", 'Mango', 'Apple']
#
#     def choose(fruit):
#         print(c)
#
#     choose('Grape')
# Output yang benar adalah
# a. fruit
# b. Grape
# c. Apple --> Jawaban
# d. Banana
#
# Jawaban
# Jawaban yang benar adalah: c. Apple
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# a, b, c = ["Banana", "Mango", "Apple"]
#
# def choose(fruit):
#     print(c)
#
# choose('Grape')
#
# Penjelasan Kode
#
# 1. Deklarasi Variabel a, b, dan c:
#     * Pada baris pertama, kita mendefinisikan tiga variabel a, b, dan c dengan nilai masing-masing dari list
#     ["Banana", "Mango", "Apple"].
#
#     * Setelah ini, a berisi "Banana", b berisi "Mango", dan c berisi "Apple".
#
# 2. Fungsi choose:
#     * Fungsi choose menerima satu parameter fruit. Namun, parameter fruit tidak digunakan di dalam fungsi.
#
#     * Di dalam fungsi, hanya ada satu statement print(c), yang akan mencetak nilai dari variabel c.
#
# 3. Pemanggilan Fungsi choose('Grape'):
#     * Ketika choose('Grape') dipanggil, nilai 'Grape' diberikan sebagai argumen untuk parameter fruit,
#     tetapi nilai ini tidak digunakan di dalam fungsi.
#
#     * Di dalam fungsi, perintah print(c) akan mencetak nilai dari variabel c, yang telah diinisialisasi sebagai "Apple" di luar fungsi.
#
# 4. Output:
#     * Karena c berisi "Apple", output dari print(c) adalah Apple.
#
# Kesimpulan
# * Jawaban yang benar adalah c. Apple karena variabel c telah diinisialisasi dengan nilai "Apple" di luar fungsi,
# dan fungsi choose hanya mencetak nilai c, yang mengacu pada "Apple".
#
# Alasan Pilihan Lainnya Salah
#
# a. fruit — Salah, karena fruit adalah parameter dalam fungsi yang tidak digunakan atau dicetak.
#
# b. Grape — Salah, karena 'Grape' hanyalah argumen yang diberikan ke parameter fruit, tetapi tidak dicetak oleh fungsi.
#
# d. Banana — Salah, karena c berisi "Apple", bukan "Banana".

# =============================================================================================
# Soal 24
# 24. Terdapat code sebagai berikut :
#     def tambah(angka):
#         total = 0
#         for i in angka:
#             if i % 2 == 0:
#                 total += i
#         print(total)
#
#     tambah([8,3,4,7])
#
#     Output yang benar adalah :
#     a. 22
#     b. 12 --> Jawaban
#     c. 10
#     d. 2
#
# Jawaban
# Jawaban yang benar adalah: b. 12
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# def tambah(angka):
#     total = 0
#     for i in angka:
#         if i % 2 == 0:
#             total += i
#     print(total)
#
# tambah([8, 3, 4, 7])
#
# Penjelasan Kode
#
# 1. Fungsi tambah:
#     * Fungsi tambah menerima satu parameter angka, yang diharapkan berupa list dari angka-angka.
#
#     * Di dalam fungsi, variabel total diinisialisasi dengan nilai 0. Variabel ini akan digunakan
#     untuk menyimpan jumlah dari angka-angka genap dalam list angka.
#
# 2. Loop dan Kondisi:
#     * Fungsi melakukan iterasi melalui setiap elemen i di dalam list angka.
#
#     * Untuk setiap elemen i, ada kondisi if i % 2 == 0 yang memeriksa apakah i adalah bilangan genap.
#         Jika i adalah genap (yakni jika i % 2 == 0 bernilai True), maka i akan ditambahkan ke total.
#
# 3. Pemanggilan Fungsi tambah([8, 3, 4, 7]):
#     * Fungsi dipanggil dengan argumen [8, 3, 4, 7].
#     * Mari kita hitung langkah demi langkah apa yang terjadi di dalam loop:
#     i = 8: 8 % 2 == 0 (True), maka total += 8, sehingga total menjadi 8.
#
#     i = 3: 3 % 2 == 0 (False), sehingga total tetap 8.
#
#     i = 4: 4 % 2 == 0 (True), maka total += 4, sehingga total menjadi 12.
#
#     i = 7: 7 % 2 == 0 (False), sehingga total tetap 12.
#
# 4. Output:
#     * Setelah loop selesai, total berisi 12, yang kemudian dicetak dengan print(total).
#
# Kesimpulan
# Jawaban yang benar adalah b. 12 karena jumlah dari angka-angka genap dalam list [8, 3, 4, 7] adalah 8 + 4 = 12.
#
# Alasan Pilihan Lainnya Salah
# a. 22 — Salah, karena jumlah dari semua angka bukan genap di list ini.
#
# c. 10 — Salah, karena jumlah dari angka-angka genap adalah 12, bukan 10.
#
# d. 2 — Salah, karena ini bukan hasil yang benar dari penjumlahan angka-angka genap dalam list.
# Ringkasan

# =============================================================================================
# Soal 25
# 25. Terdapat code sebagai berikut :
# a = 77
#
# def myFunction():
#     global x
#     x = 5
#     print(f'ini adalah variabel dalam fungsi:', a)
#
# x = 100
#
# myFunction()
#
# print(f'ini adalah variabel di luar fungsi:', x)
#
# Output yang benar adalah
# a. ini adalah variabel dalam fungsi: 77 | ini adalah variable di luar fungsi: 5  --> Jawaban
# b. ini adalah variabel dalam fungsi: 5 | ini adalah variable di luar fungsi: 100
# c. ini adalah variabel dalam fungsi: 77 | ini adalah variable di luar fungsi: 100
# d. ini adalah variabel dalam fungsi: 100 | ini adalah variable di luar fungsi: 5
#
# Jawaban
# Jawaban yang benar adalah: a. ini adalah variabel dalam fungsi: 77 | ini adalah variable di luar fungsi: 5
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# a = 77
#
# def myFunction():
#     global x
#     x = 5
#     print(f'ini adalah variabel dalam fungsi:', a)
#
# x = 100
#
# myFunction()
#
# print(f'ini adalah variabel di luar fungsi:', x)
#
# 1. Penjelasan Kode
#     * Deklarasi Variabel Global a:
#     Variabel a dideklarasikan di luar fungsi dengan nilai 77. Variabel ini bersifat global dan
#     dapat diakses dari dalam fungsi.
#
# 2. Fungsi myFunction dan Penggunaan global x:
#     * Di dalam myFunction, kita mendeklarasikan x sebagai global dengan menggunakan global x.
#     Ini berarti bahwa setiap perubahan pada x di dalam fungsi akan mempengaruhi variabel x di ruang lingkup global.
#
#     * Kemudian, x diatur ulang menjadi 5 di dalam fungsi, dan karena x adalah variabel global,
#       nilai ini akan berlaku di seluruh program, termasuk di luar fungsi.
#
#     * Fungsi myFunction juga mencetak nilai variabel a, yang bernilai 77.
#
# 3. Pemanggilan Fungsi myFunction():
#     * Ketika myFunction() dipanggil, variabel x diubah menjadi 5 secara global.
#
#     * Output dari print(f'ini adalah variabel dalam fungsi:', a) akan menjadi ini adalah variabel
#       dalam fungsi: 77 karena a memiliki nilai 77.
#
# 4. Cetakan di Luar Fungsi:
#     * Setelah myFunction() selesai dieksekusi, kita mencetak nilai x di luar fungsi. Karena x
#         telah diubah menjadi 5 di dalam fungsi menggunakan global x, maka cetakan di luar fungsi
#         akan menunjukkan x sebagai 5.
#
# Kesimpulan
# Jawaban yang benar adalah a. ini adalah variabel dalam fungsi: 77 | ini adalah variable di luar fungsi: 5.
#
# Alasan Pilihan Lainnya Salah
#
# b. ini adalah variabel dalam fungsi: 5 | ini adalah variable di luar fungsi: 100 —
#    Salah, karena nilai a tetap 77, dan x diubah menjadi 5 dalam fungsi.
#
# c. ini adalah variabel dalam fungsi: 77 | ini adalah variable di luar fungsi: 100 —
#     Salah, karena x telah diubah menjadi 5 secara global oleh fungsi myFunction.
#
# d. ini adalah variabel dalam fungsi: 100 | ini adalah variable di luar fungsi: 5 —
#    Salah, karena a adalah 77, bukan 100.

# =============================================================================================
# Soal 26
# 26. Terdapat code sebagai berikut :
# # function
# def description(a, b, c):
#     if c == True:
#         c = 'Animation'
#     else:
#         c = 'Live'
#
#     print(f'This movie title is {a.upper()}. It\'s produced in {b + 10}. It\'s categorized as {c} movie.')
#
# Output: This movie title is MADAGASCAR. It's produced in 2010. It's categorized as Animation movie. Nilai yang tepat untuk mengisi X,Y, dan Z adalah
# a. X = 'madagascar' , Y = True , Z = 2020
# b. X = 'madagascar' , Y = 2020 , Z = True
# c. X = 'madagascar' , Y = 2010 , Z = True --> Jawaban
# d. X = 'madagascar' , Y = 2000 , Z = True
#
# Jawaban
# Jawaban yang benar adalah: c. X = 'madagascar' , Y = 2010 , Z = True
#
# Penjelasan
# Mari kita analisis kode berikut:
#
# def description(a, b, c):
#     if c == True:
#         c = 'Animation'
#     else:
#         c = 'Live'
#
#     print(f'This movie title is {a.upper()}. It\'s produced in {b + 10}. It\'s categorized as {c} movie.')
#
# Fungsi description memiliki tiga parameter: a, b, dan c, yang akan memengaruhi output sesuai dengan kondisi dan operasi berikut:
#
# 1. Parameter a:
#     * a adalah judul film, yang kemudian dikonversi menjadi huruf besar dengan a.upper().
#
#     *  output yang diinginkan, kita tahu bahwa judul film harus MADAGASCAR, sehingga a harus berisi 'madagascar'
#     dalam huruf kecil untuk memenuhi kebutuhan a.upper().
#
# 2. Parameter b:
#     * b adalah tahun produksi, tetapi dalam output b ditampilkan sebagai b + 10.
#
#     * Dari output yang diinginkan, tahun produksi adalah 2010. Jadi,
#     kita perlu mencari nilai b sedemikian rupa sehingga b + 10 = 2010.
#
#     * Solusi untuk ini adalah: b = 2010 − 10 = 2000
#
#     * Oleh karena itu, b harus bernilai 2000.
#
# 3. Parameter c:
#     * c adalah kategori film yang berdasarkan kondisi:
#         * Jika c == True, maka c diubah menjadi 'Animation'.
#
#         * Jika c == False, maka c diubah menjadi 'Live'.
#
#     * Dari output yang diinginkan, kategori film adalah Animation, sehingga c harus True agar memenuhi kondisi ini.
#
# Kesimpulan
# Untuk menghasilkan output:
#
#
# This movie title is MADAGASCAR. It's produced in 2010. It's categorized as Animation movie.
# Nilai yang tepat untuk X, Y, dan Z adalah:
#
# X = 'madagascar'
# Y = 2000
# Z = True
# Alasan Pilihan Lainnya Salah
# a. X = 'madagascar', Y = True, Z = 2020 — Salah, karena Y seharusnya angka tahun, bukan True.
# b. X = 'madagascar', Y = 2020, Z = True — Salah, karena Y + 10 akan menjadi 2030, bukan 2010.
# d. X = 'madagascar', Y = 2000, Z = True — Benar, ini adalah opsi yang benar sesuai penjelasan di atas.
# =============================================================================================
# Soal 27
# 27. Terdapat code sebagai berikut :
#
#     listAngka = [1,2,3,4]
#
#     mapPangkatTIga = . . .
#
#     print(list(mapPangkatTiga))
#
# Output: [1, 8, 27, 64]
# Code yang cocok untuk mengisi variable mapPangkatTiga adalah
# a. map(lambda a: pow(a,3), listAngka) --> Jawaban
# b. map(lambda a = pow(a,3), listAngka)
# c. map(lambda a: pow[a,3], listAngka)
# d. lambda (a: pow(a,3), listAngka)
#
# Jawaban
# Jawaban yang benar adalah: a. map(lambda a: pow(a,3), listAngka)
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# listAngka = [1, 2, 3, 4]
#
# mapPangkatTiga = map(lambda a: pow(a, 3), listAngka)
#
# print(list(mapPangkatTiga))
#
# Penjelasan Kode
#
# 1. Fungsi map():
#     * Fungsi map() digunakan untuk menerapkan suatu fungsi ke setiap item dalam iterable (dalam hal ini, listAngka).
#
#     * map() membutuhkan dua argumen:
#         * Fungsi yang akan diterapkan (dalam bentuk lambda atau fungsi lain).
#
#         * Iterable yang akan diterapkan fungsi tersebut pada setiap elemennya.
#
# 2.  Lambda Function dan pow():
#     * Lambda function lambda a: pow(a, 3) adalah fungsi anonim yang mengambil satu parameter a
#     dan mengembalikan hasil dari pow(a, 3), yaitu a pangkat tiga.
#
#     * Fungsi pow(a, 3) mengembalikan hasil dari a dipangkatkan 3.
#
# 3. Hasil map():
#     * Ketika kita menerapkan map(lambda a: pow(a, 3), listAngka), setiap elemen dalam listAngka akan dipangkatkan tiga.
#
#     * Hasilnya adalah map object yang perlu diubah menjadi list dengan list(mapPangkatTiga)
#     untuk mendapatkan output dalam bentuk list.


# =============================================================================================
# Soal 28
# Terdapat code sebagai berikut :
#
#     listBilangan = [7,8,9,10,11,12]
#
#     print(list(filter(lambda x : x%3==0 , listBilangan)))
#
# Output yang benar adalah
# a. [7, 8, 9]
# b. [10, 11, 12]
# c. [7, 8, 10, 11]
# d. [9, 12] --> Jawaban
#
# Jawaban
# Jawaban yang benar adalah: d. [9, 12]
#
# Penjelasan
# Mari kita analisis kode berikut ini:
#
# listBilangan = [7, 8, 9, 10, 11, 12]
#
# print(list(filter(lambda x: x % 3 == 0, listBilangan)))
# Penjelasan Kode
#
# 1. Fungsi filter():
#     * Fungsi filter() digunakan untuk menyaring elemen-elemen dalam sebuah iterable (dalam hal ini, listBilangan)
#     berdasarkan suatu kondisi.
#
#     * filter() membutuhkan dua argumen:
#         * Fungsi yang mengembalikan True atau False (dalam bentuk lambda function atau fungsi lainnya).
#
#         * Iterable yang akan disaring.
#
#         * filter() hanya akan menyertakan elemen-elemen dalam hasil jika fungsi tersebut
#         mengembalikan True untuk elemen tersebut.
#
# 2. Lambda Function lambda x: x % 3 == 0:
#     * Lambda function ini memeriksa apakah suatu bilangan x habis dibagi 3 (dengan sisa 0).
#
#     * Jika x % 3 == 0 bernilai True, maka x akan dimasukkan ke dalam hasil; jika False, maka x akan diabaikan.
#
# 3. Penerapan filter() pada listBilangan:
#     * Kode filter(lambda x: x % 3 == 0, listBilangan) akan menyaring elemen-elemen dari
#         listBilangan yang habis dibagi 3.
#
# 4. Evaluasi Elemen dalam listBilangan:
#     Mari kita lihat setiap elemen dalam listBilangan untuk menentukan apakah habis dibagi 3:
#     * 7 % 3 == 1 (False) → tidak termasuk.
#     * 8 % 3 == 2 (False) → tidak termasuk.
#     * 9 % 3 == 0 (True) → termasuk.
#     * 10 % 3 == 1 (False) → tidak termasuk.
#     * 11 % 3 == 2 (False) → tidak termasuk.
#     * 12 % 3 == 0 (True) → termasuk.
#
# 5. Hasil filter():
#     * Hanya 9 dan 12 yang memenuhi kondisi x % 3 == 0.
#     * Hasil dari filter() akan berupa [9, 12].
#
# Kesimpulan
#     * Jawaban yang benar adalah d. [9, 12] karena hanya angka 9 dan 12 dalam listBilangan yang habis dibagi 3.
#
# Kode Lengkap
# Berikut adalah kode lengkap yang menghasilkan output yang diinginkan:
#
# listBilangan = [7, 8, 9, 10, 11, 12]
#
# print(list(filter(lambda x: x % 3 == 0, listBilangan)))

# =============================================================================================
#

