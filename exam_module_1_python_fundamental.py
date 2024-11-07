#================================================================================================
# Soal 1
Manakan pernyataan yang BENAR terkait dengan break dan continue pada looping statement ?
Pilihlah jawaban yang
    a. Statement setelah continue dalam blok perulangan tidak akan di jalankan
    b. Semua benar
    c. Statement setelah break dalam blok perulangan tetap akan dijalankan
    d. Break digunakan untuk melanjutkan ke proses perulangan berikutnya
    e. Continue digunakan untuk keluar dari blok perulangan

Jawaban yang benar adalah:

a. Statement setelah continue dalam blok perulangan tidak akan dijalankan.
Penjelasan:

* continue digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya dalam perulangan,
    tanpa mengeksekusi statement setelahnya di dalam blok perulangan.

* break digunakan untuk keluar dari seluruh perulangan. Saat break dieksekusi, perulangan langsung berhenti,
    dan statement setelah perulangan (bukan dalam blok perulangan) yang akan dijalankan.
    Mari kita lihat contoh kode Python untuk memverifikasi perbedaan break dan continue:

print("Contoh penggunaan continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)  # Statement ini tidak akan dijalankan saat i == 2

print("\nContoh penggunaan break:")
for i in range(5):
    if i == 2:
        break
    print(i)  # Perulangan berhenti sepenuhnya saat i == 2

Output yang akan dihasilkan:
Contoh penggunaan continue:
0
1
3
4

Contoh penggunaan break:
0
1

* Pada contoh continue, ketika i == 2, loop melewati print(i) dan melanjutkan ke iterasi berikutnya,
    jadi 2 tidak dicetak.

* Pada contoh break, ketika i == 2, loop langsung berhenti, jadi angka setelah 1 tidak dicetak.
#================================================================================================
# Soal 2
Buatkan semua function yang dapat menambahkan semua angkat dalam list

def sum_all(numbers):
    total = 0
    for x in numbers:
        if x%2 == 0:
            total += x
    print(total)

Jika argument diisi dengan [8,4,7,2,5], maka output yang dihasilkan adalah ?
a. 14
b. 9
c. 15
d. 26
e. 12

Penjelasan:

1. Inisialisasi Fungsi:
    * Fungsi sum_all(numbers) menerima satu parameter numbers, yang diharapkan menjadi list angka.

2.  Logika dalam Fungsi:
    * total diinisialisasi dengan nilai 0.
    * Fungsi melakukan iterasi pada setiap elemen x dalam numbers.
    * Jika x adalah angka genap (x % 2 == 0), maka x akan ditambahkan ke total.
    * Setelah loop selesai, nilai total dicetak.

3. Memasukkan Argument:
    * Jika numbers = [8, 4, 7, 2, 5], fungsi akan menambahkan hanya angka genap di dalam list, yaitu 8, 4, dan 2.
    Jadi:
            8 + 4 + 2 = 14

Output yang dihasilkan: Pilihan a. 14

Kode Python untuk memverifikasi:

def sum_all(numbers):
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total += x
    print(total)

# Memanggil fungsi dengan argument [8, 4, 7, 2, 5]
sum_all([8, 4, 7, 2, 5])

#================================================================================================
# Soal 3
Terdapat code sebagai berikut :
x, y, z = ['Hello', 'I am', 'John']
def say (word) :
    print(x)
say('Python')

Dari code di atas, hasil apa kah yang muncul ?
a. "Hello i am John"
b. "John"
c. "Hello"
d. "Python"
e. "I am"
#================================================================================================
# Soal 4

Penjelasan:

1. Inisialisasi Variabel:
    * x, y, dan z diinisialisasi dengan nilai dari list ['Hello', 'I am', 'John'].

    * Jadi, x = 'Hello', y = 'I am', dan z = 'John'.

2.  Fungsi say:
    * Fungsi say menerima satu parameter word, tetapi parameter ini tidak digunakan dalam tubuh fungsi.

    * Di dalam fungsi say, hanya ada pernyataan print(x), yang akan mencetak nilai dari x.

3.  Memanggil Fungsi say('Python'):
    * Ketika say('Python') dipanggil, fungsi akan mencetak nilai x.

    * Karena x telah diinisialisasi dengan nilai 'Hello', maka print(x) akan mencetak 'Hello'.

Jadi, output dari kode ini adalah: Pilihan c. "Hello"

Kode Python untuk memverifikasi:

x, y, z = ['Hello', 'I am', 'John']

def say(word):
    print(x)

say('Python')

Output yang akan dicetak: Hello
#================================================================================================
# Soal 5

Terdapat dictionary sebagai berikut :

Dict = {
    'nama' : 'Rony',
    'kelas' : '3B',
    'nilai' : 80
}

Kita perlu untuk mengganti value dalam key 'nilai menjadi 90.'
Maka code yang tepat adalah :
a. Dict.setdefault(key = 'nilai', value = 90)
b. Dict.change({'nilai':90})
c. Dict['nilai'] = 90
d. Dict['nilai'] : 90
e. Dict.items({'nilai:90'})

Penjelasan:

Kita perlu mengganti nilai pada key 'nilai' dari 80 menjadi 90.

*   Pilihan a: Dict.setdefault(key = 'nilai', value = 90)
        * setdefault digunakan untuk menambahkan key-value baru jika key tersebut belum ada dalam dictionary.
            Namun, jika key 'nilai' sudah ada, nilai aslinya tidak akan diubah. Jadi, ini bukan pilihan yang tepat.

*   Pilihan b: Dict.change({'nilai':90})
        * change bukan metode yang valid dalam dictionary di Python, jadi ini akan menghasilkan error.

* Pilihan c: Dict['nilai'] = 90
        * Ini adalah cara yang benar untuk mengganti nilai dalam dictionary. Kita dapat langsung mengubah nilai
                dengan mengakses key 'nilai' dan menetapkan nilai baru 90.

* Pilihan d: Dict['nilai'] : 90
        * Ini adalah sintaks yang salah karena tanda titik dua : tidak digunakan untuk mengubah nilai.
        Kita menggunakan tanda sama dengan = untuk menetapkan nilai baru.

* Pilihan e: Dict.items({'nilai:90'})
        * items() bukan metode yang digunakan untuk mengubah nilai dalam dictionary;
            metode ini hanya mengembalikan pasangan key-value dalam bentuk tuple.

Jawaban yang benar adalah: Pilihan c. Dict['nilai'] = 90

Kode Python untuk memverifikasi:

Dict = {
    'nama': 'Rony',
    'kelas': '3B',
    'nilai': 80
}

# Mengubah nilai pada key 'nilai'
Dict['nilai'] = 90

print(Dict)

Output yang akan dicetak:

{'nama': 'Rony', 'kelas': '3B', 'nilai': 90}

Dengan demikian, nilai pada key 'nilai' telah berhasil diubah menjadi 90

#================================================================================================
# Soal 6
Temukan pasangan yang tepat! Apa perbedaan methods.append() dan .extend() pada Python List ?
Pilihlah jawaban yang tepat
a. Append menambahkan tiap element dari suatu iterable ke dalam list. Extend menambahkan suatu object
   di akhir sebuah list

b. Append menduplikasi tiap element dalam list, ke posisi paling belakang list. Extend menambahkan suatu
   object di akhir list

c. Append menambahkan suatu object di akhir list. Extend menambah tiap element dari suatu iterable ke dalam list

d. Append menghapus element pada akhir list. Extend menghapus element pada awal list

e. Append menambah element dari depan list. Extend menambah element dari belakang list

Jawaban yang benar adalah:

Pilihan: c. Append menambah suatu object di akhir list.
            Extend menambah tiap elemen dari suatu iterable ke dalam list

Penjelasan:

    * .append(): Metode ini menambahkan satu elemen ke akhir list.
        Elemen yang ditambahkan bisa berupa tipe data apapun (angka, string, list, dll),
        tetapi elemen tersebut ditambahkan sebagai satu objek di akhir list.

    * .extend(): Metode ini menambahkan setiap elemen dari suatu iterable (seperti list atau tuple) ke list.
        Jadi, jika kita menggunakan .extend() dengan list lain, maka setiap elemen dari list tersebut
        akan ditambahkan ke list asli satu per satu, bukan sebagai satu objek tunggal.

Contoh Kode Python untuk Memverifikasi:

# Menggunakan .append()
list1 = [1, 2, 3]
list1.append([4, 5])  # Menambahkan list sebagai satu objek
print("Setelah append:", list1)  # Output: [1, 2, 3, [4, 5]]

# Menggunakan .extend()
list2 = [1, 2, 3]
list2.extend([4, 5])  # Menambahkan setiap elemen dari list
print("Setelah extend:", list2)  # Output: [1, 2, 3, 4, 5]

Output:

Setelah append: [1, 2, 3, [4, 5]]
Setelah extend: [1, 2, 3, 4, 5]

Penjelasan Output:

    * Pada contoh .append(), [4, 5] ditambahkan sebagai satu objek di akhir list1,
    sehingga hasilnya adalah [1, 2, 3, [4, 5]].

    * Pada contoh .extend(), setiap elemen dari [4, 5] ditambahkan secara individual ke list2,
    sehingga hasilnya adalah [1, 2, 3, 4, 5].

#================================================================================================
# Soal 7
Function encryptor digunakan untuk mengenkripsi sebuah pesan dengan mengganti setiap huruf
dengan huruf yang berjarak 2 huruf di depannya. Misalnya:

A menjadi C
Y menjadi A
Z menjadi B
Kode yang diberikan:

def encryptor(word):
    abjad = 'abcdefghijklmnopqrstuvwxyz'
    words = word.lower()
    encrypt = ''
    for c in words:
        if c != ' ':
            index = ________  # isi di sini
            encrypt += abjad[index].upper()
        else:
            encrypt += ' '
    return encrypt

print(encryptor('ridho'))

isilah kekosongan pada variable index di atas tengan code yang tepat !
a. (abjad.index(c) + 2)/len(abjad)
b. (abjad.index(c) + 2)%len(abjad)//2
c. (abjad.index(c) + 2)%len(abjad)
d. (abjad.index(c) + 2)*len(abjad)
e. (abjad.index(c) + 2//len(abjad)

Output yang diharapkan: TKFJQ

Penjelasan:

1. Kita ingin setiap huruf digeser dua posisi ke depan dalam alfabet. Jika posisi melebihi panjang alfabet
    (misalnya, Y atau Z),  kita perlu melingkar kembali ke awal alfabet.

2. Untuk menghitung indeks baru setelah pergeseran, kita gunakan:
index = (abjad.index(c) + 2) % len(abjad)

    * abjad.index(c) memberikan posisi dari huruf c dalam string abjad.

    * + 2 menambahkan dua posisi ke indeks saat ini.

    * % len(abjad) memastikan kita melingkar kembali ke awal alfabet jika indeks melebihi panjang alfabet (26).

Jawaban yang benar adalah: Pilihan c. (abjad.index(c) + 2) % len(abjad)

Kode Python Lengkap untuk Verifikasi:

def encryptor(word):
    abjad = 'abcdefghijklmnopqrstuvwxyz'
    words = word.lower()
    encrypt = ''
    for c in words:
        if c != ' ':
            index = (abjad.index(c) + 2) % len(abjad)
            encrypt += abjad[index].upper()
        else:
            encrypt += ' '
    return encrypt

print(encryptor('ridho'))  # Output yang diharapkan: TKFJQ

Output yang akan dicetak:

TKFJQ

engan demikian, jawaban yang benar adalah pilihan c. (abjad.index(c) + 2) % len(abjad)
#================================================================================================
# Soal 8

Soal: Pernyataan yang tepat tentang While Loop?

Pilihan Jawaban:

a. Semua jawaban benar.
b. Kita tidak dapat melakukan nested While Loop (While Loop dalam While Loop).
c. While loop hanya melakukan looping sekali.
d. Kita tidak dapat menyelipkan If Else di dalam While Loop.
e. While Loop adalah sebuah method yang memungkinkan kita untuk mengeksekusi code selama suatu kondisi masih terpenuhi
    atau dengan kata lain suatu kondisi masih True.

awaban yang benar adalah:
e. While Loop adalah sebuah method yang memungkinkan kita untuk mengeksekusi code selama suatu kondisi masih terpenuhi
    atau dengan kata lain suatu kondisi masih True.

Penjelasan:

*   While Loop dalam Python adalah perulangan yang akan terus berjalan selama kondisi yang diberikan bernilai True.
    Jika kondisi menjadi False, loop akan berhenti.

* Kita dapat melakukan nested While Loop, yaitu While Loop di dalam While Loop lainnya.

*   While Loop dapat melakukan perulangan lebih dari satu kali selama kondisi masih True.

* Kita dapat menyelipkan pernyataan if-else di dalam While Loop.

# Contoh While Loop dengan kondisi True
count = 0
while count < 3:
    print("Perulangan ke:", count)
    count += 1

# Contoh While Loop dengan nested While Loop dan If-Else di dalamnya
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        if j % 2 == 0:
            print(f"i: {i}, j: {j} - Genap")
        else:
            print(f"i: {i}, j: {j} - Ganjil")
        j += 1
    i += 1

Output:

Perulangan ke: 0
Perulangan ke: 1
Perulangan ke: 2
i: 1, j: 1 - Ganjil
i: 1, j: 2 - Genap
i: 2, j: 1 - Ganjil
i: 2, j: 2 - Genap
i: 3, j: 1 - Ganjil
i: 3, j: 2 - Genap

Pada contoh di atas:

* While Loop pertama melakukan perulangan sebanyak tiga kali.

* While Loop kedua adalah nested While Loop, dan di dalamnya terdapat pernyataan if-else untuk
menentukan apakah j ganjil atau genap.
#================================================================================================
# Soal 9

Terdapat list ['Andi', 'Budi', 'Caca', 'Dedi']. Jika kita ingin mengetahui posisi index elemen 'Dedi',
metode apa yang digunakan?

Pilihan Jawaban:

a. List.find()
b. List.where()
c. List.index()
d. List.pop()
d. List.isin()

Jawaban yang benar adalah: Pilihan c. List.index()

Penjelasan:

    * Metode index() pada list digunakan untuk mencari posisi (indeks) dari elemen tertentu dalam list.

    * Jika elemen yang dicari ada dalam list, metode ini akan mengembalikan indeksnya. Jika elemen tidak ditemukan,
    maka akan terjadi error ValueError.

Contoh Kode Python untuk Memverifikasi:
# List yang diberikan
my_list = ['Andi', 'Budi', 'Caca', 'Dedi']

# Mencari indeks dari elemen 'Dedi'
index_dedi = my_list.index('Dedi')
print("Indeks dari 'Dedi':", index_dedi)

Output yang akan dicetak:

Indeks dari 'Dedi': 3

Penjelasan Output:

Dalam list my_list, elemen 'Dedi' berada pada indeks ke-3.

#================================================================================================
# Soal 10
Code
A : 33
b = 200
if b > a :
print("b is greater than a")

Jik code ini kita run apakah yang akan terjadi ?
a. Error karena permasalahan indentation

b. Error karena setiap kita selesai mendeklarasi Conditional Statement (if b > a) harus diakhiri = 'bukan ':'

c. Hasil yang muncul adalah "b is greater than a"

d. Hasil yang muncul adalah Boolean True

e. Error karena kesalahan deklarasi simbol condition

Penjelasan :

Kode yang diberikan:

a = 33
b = 200
if b > a :
print("b is greater than a")

Analisis:

1. Kode ini memiliki masalah pada indentation (pengaturan spasi/tab). Dalam Python,
    statement di dalam blok if harus diindentasi. Pada kode di atas, baris print("b is greater than a")
    tidak diindentasi sehingga akan menyebabkan error.

2.  Jika kode ini dijalankan, akan menghasilkan error karena Python membutuhkan indentation yang benar
    untuk menandakan bahwa print("b is greater than a") adalah bagian dari blok if.

3.  Pilihan jawaban yang sesuai adalah:
    a. Error karena permasalahan indentation

Kode Python yang benar:
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Menambahkan indentation yang benar

Penjelasan Output:

* Setelah memperbaiki indentation, kode ini akan berjalan dengan benar.

* Karena b (200) lebih besar dari a (33), kondisi if b > a bernilai True,
    dan Python akan mengeksekusi print("b is greater than a").

* Output yang akan dicetak adalah:
    b is greater than a

#================================================================================================
# Soal 11

Diberikan function greeting yang memiliki tiga parameter (x, y, z) dan berfungsi untuk mencetak kalimat salam
    sesuai format tertentu. Output yang diharapkan adalah:

Hello my name is Fita. Next year, I am 26 years old. And I am Married woman.

Kode Function:

def greeting(x, y, z):
    if z == True:
        z = 'Married'
    else:
        z = 'Not Married'

    print('''
    Hello my name is {}. Next year, I am {} years old. And I am {} woman.
    '''.format(x.capitalize(), y+1, z))

Expected Output:

Hello my name is Fita. Next year, I am 26 years old. And I am Married woman.

Analisis:

Untuk menghasilkan output seperti di atas:

    1.Nama harus menjadi "Fita". Ini berarti parameter x harus diberi nilai "Fita".

    2. Umur tahun depan adalah 26, yang berarti parameter y saat ini adalah 25 karena akan ditambahkan 1 (y+1).

    3. Status pernikahan adalah "Married", yang berarti parameter z harus bernilai True
        untuk memenuhi kondisi if z == True:.

Jawaban yang benar adalah: Pilihan c. I = 'Fita', II = 25, III = True

Kode Python untuk Memverifikasi:

def greeting(x, y, z):
    if z == True:
        z = 'Married'
    else:
        z = 'Not Married'

    print('''
    Hello my name is {}. Next year, I am {} years old. And I am {} woman.
    '''.format(x.capitalize(), y+1, z))

# Memanggil function dengan parameter yang sesuai
greeting('Fita', 25, True)

Output yang akan dicetak:

Hello my name is Fita. Next year, I am 26 years old. And I am Married woman.

Dengan parameter x = 'Fita', y = 25, dan z = True, function akan menghasilkan output yang diharapkan.
#================================================================================================
# Soal 12

kode berikut:

frase = 'Skill Accelerator Bootcamp'
print(frase[2:-2])

Penjelasan:

1. String Slicing frase[2:-2]:
    * frase[2:-2] mengambil substring dari indeks ke-2 hingga indeks sebelum -2 dari string frase.

    * Dalam Python:
        * Indeks positif dimulai dari kiri (0 untuk 'S').

        * Indeks negatif dimulai dari kanan (-1 untuk karakter terakhir 'p').

2. Langkah-langkah Slicing:
    * frase[2:] berarti mengambil karakter dari indeks ke-2 hingga akhir string.

        * frase[2:] pada string 'Skill Accelerator Bootcamp' akan menghasilkan 'ill Accelerator Bootcamp'.

    * frase[:-2] berarti mengambil karakter dari awal string hingga dua karakter terakhir.

        frase[:-2] akan menghasilkan 'Skill Accelerator Bootca'.

Jadi, kombinasi frase[2:-2] menghasilkan substring yang dimulai dari indeks ke-2 hingga sebelum dua karakter terakhir, yaitu: 'ill Accelerator Bootca'.
Jawaban yang benar adalah: Pilihan ill Accelerator Bootca

Kode Python untuk Verifikasi:

frase = 'Skill Accelerator Bootcamp'
print(frase[2:-2])  # Output yang diharapkan: 'ill Accelerator Bootca'

Output yang akan dicetak:

ill Accelerator Bootca

#================================================================================================
# Soal 13
Soal: Manakah simbol yang tepat untuk menggambarkan kondisi "Greater than or equal to" dalam Python?

Jawaban yang benar adalah: Pilihan >=

Penjelasan:

    * Simbol >= digunakan dalam Python untuk mengecek apakah suatu nilai lebih besar atau sama dengan nilai lainnya.
    Ini disebut "Greater than or equal to."

    * Dalam Python, operator perbandingan ini digunakan dalam pernyataan if untuk menjalankan kode berdasarkan
    kondisi tersebut.

Contoh Kode Python untuk Memverifikasi:

a = 10
b = 8

# Menggunakan operator >=
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")

Output yang akan dicetak:

a is greater than or equal to b

Pada contoh di atas, karena a (10) lebih besar dari b (8), maka kondisi a >= b bernilai True,
sehingga output yang dicetak adalah "a is greater than or equal to b."
#================================================================================================
# Soal 14
Diberikan string 'Halo nama saya Randy'. Kita ingin mengubah string ini menjadi list ['Halo', 'Nama', 'Saya', 'Randy'], di mana setiap kata dimulai dengan huruf kapital.

Kode yang diberikan:

a = 'Halo nama saya Randy'
b = [i.________() for i in a.split()]

Pilihan Jawaban:

a. islower()
b. capitalize()
c. istitle()
d. lower()
e. upper()

Jawaban yang benar adalah: Pilihan b. capitalize()

Penjelasan:

* Fungsi capitalize() mengubah huruf pertama dari setiap kata menjadi huruf kapital dan sisanya menjadi huruf kecil.

* Dalam konteks list comprehension [i.capitalize() for i in a.split()], setiap kata yang dihasilkan dari a.split()
    akan dimodifikasi menjadi format kapital pada huruf pertama, yang sesuai dengan format yang diinginkan.

Contoh Kode Python untuk Verifikasi:

a = 'Halo nama saya Randy'
b = [i.capitalize() for i in a.split()]
print(b)

Output yang akan dicetak:

['Halo', 'Nama', 'Saya', 'Randy']

Dengan menggunakan capitalize(), kita mendapatkan list dengan setiap kata dimulai dengan
huruf kapital sesuai dengan yang diminta.
#================================================================================================
# Soal 15
Manakah simbol yang tepat untuk menggambarkan kondisi "Equals" dalam Python?

Jawaban yang benar adalah: Pilihan ==

Penjelasan:

* Dalam Python, simbol == digunakan untuk membandingkan dua nilai dan mengecek apakah mereka sama (equal).

* Jika kedua nilai sama, maka hasil perbandingan == adalah True; jika berbeda, hasilnya False.

* Perlu diperhatikan bahwa = digunakan untuk assignment (menetapkan nilai), bukan untuk perbandingan.

Contoh Kode Python untuk Memverifikasi:

a = 10
b = 10

# Menggunakan operator ==
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

Output yang akan dicetak:

a is equal to b

Pada contoh di atas, karena a dan b sama-sama bernilai 10, maka kondisi a == b bernilai True,
sehingga output yang dihasilkan adalah "a is equal to b".
#================================================================================================
# Soal 16
Apakah fungsi dari break pada looping statement?

Jawaban yang benar adalah: Pilihan
"Syntax break pada looping statement berfungsi untuk menghentikan looping statement dan mengeluarkan kita dari " \
"looping statement meskipun kondisi setelahnya masih True atau belum selesai."

Penjelasan:

* Dalam Python, break digunakan untuk menghentikan perulangan (loop) secara langsung, meskipun kondisi loop
    masih terpenuhi atau belum selesai.

* Saat break dieksekusi di dalam loop, Python akan keluar dari loop tersebut, dan eksekusi kode akan dilanjutkan pada statement setelah loop.
    Contoh Kode Python untuk Memverifikasi:

for i in range(10):
    if i == 5:
        break
    print(i)

Penjelasan Kode:

    * Loop for di atas akan berjalan dari i = 0 hingga i = 9.

    * Namun, ketika i mencapai 5, perintah break akan dijalankan, menghentikan loop.

    * Sehingga hanya angka 0 hingga 4 yang akan dicetak.

Output yang akan dicetak:

0
1
2
3
4

Pada contoh di atas, break menghentikan loop ketika i sama dengan 5, sehingga angka setelah 4 tidak dicetak.
#================================================================================================
# Soal 17
Diberikan dua list: adj = ["red", "big", "tasty"] dan fruits = ["apple", "banana", "cherry"].
Kita ingin mencetak setiap buah dengan kata sifat yang sesuai seperti pada output:

apple is red
banana is big
cherry is tasty

Kode yang perlu dilengkapi:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for ________:
    print("{} is {}".format(fruits[i], adj[i]))

Pilihan Jawaban:

a. in range(len(fruits))
b. in range(0,3)
c. in range(3)
d. in range(len(adj))

Semua jawaban benar

Jawaban yang benar adalah:
Pilihan a. i in range(len(fruits)) atau d. i in range(len(adj))


Penjelasan:

    * Kode ini membutuhkan indeks i untuk mengakses elemen-elemen dari kedua list fruits dan adj pada posisi yang sama.

    * Karena kedua list memiliki panjang yang sama (3 elemen), kita bisa menggunakan range(len(fruits))
        atau range(len(adj)) untuk mendapatkan rentang indeks yang tepat (0 hingga 2).

    * Menggunakan range(3) atau range(0, 3) juga akan berfungsi dengan benar dalam hal ini karena panjangnya sesuai.
        Jadi, jawaban "semua jawaban benar" juga dapat diterima.

Kode Python Lengkap untuk Verifikasi:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):  # atau bisa juga menggunakan range(3), range(len(adj))
    print("{} is {}".format(fruits[i], adj[i]))

Output yang akan dicetak:

apple is red
banana is big
cherry is tasty

Semua pilihan jawaban akan menghasilkan output yang diinginkan
karena semua rentang (range(3), range(len(fruits)), range(len(adj)), dan range(0, 3))
akan sesuai dengan jumlah elemen dalam kedua list.
#================================================================================================
# Soal 18
Diberikan kode berikut:

y = "Good morning"

def print_this(name):
    y = "Good evening"
    print("{a} {b}".format(a=y, b=name))

print_this("Rubben")

Pertanyaan: Manakah output yang paling tepat?

Analisis:

1. Variabel y didefinisikan di luar fungsi dengan nilai "Good morning".

2. Di dalam fungsi print_this, variabel y didefinisikan lagi dengan nilai "Good evening".
    Ini adalah variabel lokal dalam fungsi print_this yang akan digunakan di dalam fungsi ini.

3.  Saat fungsi print_this("Rubben") dipanggil, Python akan menggunakan variabel y yang ada dalam lingkup lokal fungsi,
    yaitu "Good evening".

4.  print("{a} {b}".format(a=y, b=name)) akan mencetak "Good evening Rubben" karena y dalam fungsi mengacu
pada "Good evening" dan name mengacu pada "Rubben".

Jawaban yang benar adalah: Pilihan "Good evening Rubben"

Kode Python untuk Verifikasi:

y = "Good morning"

def print_this(name):
    y = "Good evening"
    print("{a} {b}".format(a=y, b=name))

print_this("Rubben")

Output yang akan dicetak:

Good evening Rubben

#================================================================================================
# Soal 19
Apa output dari kode berikut?

a_list = []

for i in range(1,6):
    if i == 4:
        continue
    else:
        a_list.append(i)

print(a_list)

Analisis:

1. Kode ini menggunakan loop for dengan range(1, 6), yang berarti i akan mengambil nilai dari 1 hingga 5.

2.  Kondisi if i == 4 akan dilewati (dengan perintah continue) ketika i bernilai 4,
    sehingga angka 4 tidak akan ditambahkan ke dalam a_list.

3.  Untuk semua nilai i selain 4, i akan ditambahkan ke dalam a_list menggunakan a_list.append(i).

Langkah-langkah Eksekusi:

* Ketika i = 1: i ditambahkan ke a_list, sehingga a_list = [1]

* Ketika i = 2: i ditambahkan ke a_list, sehingga a_list = [1, 2]

* Ketika i = 3: i ditambahkan ke a_list, sehingga a_list = [1, 2, 3]

* Ketika i = 4: continue dieksekusi, sehingga 4 dilewati dan tidak ditambahkan ke a_list

* Ketika i = 5: i ditambahkan ke a_list, sehingga a_list = [1, 2, 3, 5]

Output yang dihasilkan: [1, 2, 3, 5]


Jawaban yang benar adalah: [1, 2, 3, 5]

Kode Python untuk Verifikasi:

a_list = []

for i in range(1, 6):
    if i == 4:
        continue
    else:
        a_list.append(i)

print(a_list)  # Output: [1, 2, 3, 5]

Output yang akan dicetak:

[1, 2, 3, 5]

#================================================================================================
# Soal 20

Diberikan kode berikut:

a = 200
b = 33
if (b == a) and (1 < 10):
    print("a and b are equal")
elif ((a > b) or (2 > 4)):
    print("a is smaller than b")
else:
    print("a is greater than b")

Pertanyaan: Jika kode ini dijalankan, hasil apa yang akan muncul?

Analisis:

1. Variabel a bernilai 200 dan b bernilai 33.

2. Pengecekan pada kondisi if:

    * (b == a) adalah False karena b (33) tidak sama dengan a (200).

    * (1 < 10) adalah True, tetapi karena (b == a) False, maka kondisi keseluruhan (b == a) and (1 < 10) menjadi False.
    Karena kondisi if False, Python akan melanjutkan ke kondisi elif.

3.  Pengecekan pada kondisi elif:
    * (a > b) adalah True karena a (200) lebih besar dari b (33).

    * (2 > 4) adalah False, tetapi karena kondisi ini dihubungkan dengan or,
    maka keseluruhan kondisi ((a > b) or (2 > 4)) menjadi True.

    * Karena kondisi elif True, pernyataan print("a is smaller than b") akan dieksekusi.

Output yang dihasilkan: "a is smaller than b"

Jawaban yang benar adalah: "a is smaller than b"

Kode Python untuk Verifikasi:

a = 200
b = 33
if (b == a) and (1 < 10):
    print("a and b are equal")
elif ((a > b) or (2 > 4)):
    print("a is smaller than b")
else:
    print("a is greater than b")

Output yang akan dicetak:

a is smaller than b

Kondisi elif dipenuhi, sehingga output yang dicetak adalah "a is smaller than b".
#================================================================================================
# 21
Diberikan kode berikut:

y = 30

def my_func():
    global x
    x = 10
    print("Value inside function:", y)

x = 20
my_func()
print("Value outside function:", x)

Pertanyaan: Manakah output yang paling tepat?

Penjelasan:

1.  Variabel y didefinisikan dengan nilai 30 di luar fungsi, sehingga y menjadi variabel global.

2.  Fungsi my_func menggunakan kata kunci global x, yang menunjukkan
    bahwa x yang ada di dalam fungsi merujuk pada variabel x global.
    * Di dalam my_func, x diubah menjadi 10 karena global x memungkinkan perubahan x dari dalam fungsi
        untuk memengaruhi x di luar fungsi.

3.  Ketika my_func() dipanggil:
    * x diubah menjadi 10.

    * print("Value inside function:", y) mencetak nilai y yang global, yaitu 30.

4. Setelah fungsi my_func dipanggil, print("Value outside function:", x)
    mencetak nilai x yang telah diubah oleh my_func, yaitu 10.

Output yang dihasilkan:

"Value inside function: 30"
"Value outside function: 10"
Jawaban yang benar adalah:

"Value inside function: 30"
"Value outside function: 10"

Kode Python untuk Verifikasi:

y = 30

def my_func():
    global x
    x = 10
    print("Value inside function:", y)

x = 20
my_func()
print("Value outside function:", x)

Output yang akan dicetak:

Value inside function: 30
Value outside function: 10

#================================================================================================
#