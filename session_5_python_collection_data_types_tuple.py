# ============================================================================================
# Syntax Tuple
# Mendefinisikan sebuah tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Menampilkan isi tuple
print(tupleContoh)
print()
# ============================================================================================
# Access Data
# Mendefinisikan sebuah tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Mengakses dan mencetak elemen-elemen tertentu dalam tuple
print(tupleContoh[0])  # Output: hello
print(tupleContoh[2])  # Output: 1
print(tupleContoh[4])  # Output: True
print()
# ============================================================================================
# Access Data Negative Indexing
# Mendefinisikan sebuah tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Mengakses elemen dengan indeks negatif
print(tupleContoh[-1])  # Output: True
print(tupleContoh[-2])  # Output: 3
print(tupleContoh[-5])  # Output: hello
print()
# ============================================================================================
# Access Data Range of Indexes
# Mendefinisikan tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Mengakses rentang elemen dengan slicing
print(tupleContoh[-4 : -1])  # Output: (1, 1, 3)
print(tupleContoh[1 : 4])    # Output: (1, 1, 3)
print(tupleContoh[-5 : 2])   # Output: ('hello', 1)
print(tupleContoh[0 : -2])   # Output: ('hello', 1, 1)
print(tupleContoh[2 : ])     # Output: (1, 3, True)
print()
# ============================================================================================
# Change Data
# Bagian pertama: Contoh yang menghasilkan error
tupleContoh = ('hello', 1, 1, 3, True)

# Percobaan mengubah nilai pada indeks 1
# tupleContoh[1] = 50  # TypeError: 'tuple' object does not support item assignment
# Bagian ini akan menghasilkan error karena tuple bersifat immutable dan tidak bisa diubah

# Bagian kedua: Cara mengubah nilai dalam tuple tanpa error
# Mengonversi tuple ke list untuk mengubah data
tupleContoh = ('hello', 1, 1, 3, True)  # Tuple asli

# Mengubah tuple ke list agar bisa diubah
listContoh = list(tupleContoh)
listContoh[1] = 50  # Mengubah elemen pada indeks 1 menjadi 50

# Mengembalikan list menjadi tuple
tupleContoh = tuple(listContoh)
print(tupleContoh)  # Output: ('hello', 50, 1, 3, True)
print()
# ============================================================================================
# Loop Through a Tuple
# Definisikan tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Loop melalui setiap elemen dalam tuple
for item in tupleContoh:
    print(item)
print()
# ============================================================================================
# Check if an Item Exists in a Tuple
# Definisikan tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Periksa apakah 'hello' ada dalam tuple
if 'hello' in tupleContoh:
    print("Ada string hello di tupleContoh")
else:
    print("string hello tidak ditemukan di tupleContoh")
print()
# ============================================================================================
# Length of Tuple
# Definisikan tuple
tupleContoh = ('hello', 1, 1, 3, True)

# Cetak panjang tuple
print(len(tupleContoh))  # Output: 5
print()
# ============================================================================================
# Create Tuple with One Item
# Membuat tuple dengan satu item
tuple1 = ('hello',)
print(tuple1)           # Output: ('hello',)
print(len(tuple1))      # Output: 1
print(type(tuple1))     # Output: <class 'tuple'>

# Contoh yang salah/bukan tuple
tuple2 = ('hello')
print(tuple2)           # Output: hello
print(type(tuple2))     # Output: <class 'str'>
print()
# ============================================================================================
# Tuple Concatenating
# Mendefinisikan dua tuple
tupleContoh = ('hello', 1, 1, 3, True)
tupleCoba = (5, 'test', False)

# Menggabungkan kedua tuple
tupleGabungan = tupleContoh + tupleCoba
print(tupleGabungan)    # Output: ('hello', 1, 1, 3, True, 5, 'test', False)
print()
# ============================================================================================
# Find Index
# Mendefinisikan tuple
tupleContoh = ('eddie', 'baron', 'andi', 'charlie', 'samson')

# Mencari index dari elemen 'andi'
indexYgDicari1 = tupleContoh.index('andi')
print(indexYgDicari1)    # Output: 2

# Mencari index dari elemen 'bernard' (yang tidak ada di dalam tuple)
try:
    indexYgDicari2 = tupleContoh.index('bernard')
    print(indexYgDicari2)
except ValueError:
    print("Error: 'bernard' tidak ditemukan dalam tuple")
print()
# ============================================================================================
# Tuple inside Tuple
# Mendefinisikan tuple 'things' dengan tuple di dalamnya
things = (
    ('red pen', 'blue pen'),
    ('analog clock', 'digital clock'),
    ('futsal shoes', 'badminton shoes')
)

# Menampilkan struktur awal dari 'things'
print("Tuple asli 'things':", things)

# Mengakses elemen di dalam tuple yang bersarang
# things[2] memberikan tuple ketiga ('futsal shoes', 'badminton shoes')
print("Mengakses tuple ketiga:", things[2])

# things[2][1] memberikan elemen kedua di dalam tuple ketiga, yaitu 'badminton shoes'
print("Mengakses item kedua di tuple ketiga:", things[2][1])

# Penjelasan:
# Karena tuple bersifat immutable, kita tidak dapat langsung memodifikasi elemen seperti `things[2][1] = 'sesuatu'`.
# Setiap upaya untuk melakukannya akan menghasilkan TypeError. Kode di atas hanya menunjukkan cara mengakses item.

# ============================================================================================













