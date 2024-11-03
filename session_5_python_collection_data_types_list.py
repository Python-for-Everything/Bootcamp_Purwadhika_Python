# List Introduction
# Membuat list yang berisi benda-benda sesuai dengan gambar
list_benda = ["buku", "pena biru", "album foto", "laptop", "pena merah"]

# Menampilkan seluruh isi list
print("Daftar benda:", list_benda)

# Menampilkan setiap item dalam list secara individual menggunakan loop
print("Daftar benda satu per satu:")
for benda in list_benda:
    print("-", benda)
print()

# List Introduction 2
print()
# Mendefinisikan list things sesuai dengan item pada gambar
things = ["buku", "pena biru", "album foto", "laptop", "pena merah"]

# Menampilkan seluruh isi list
print("Isi dari list things:", things)

# Mengakses setiap item dalam list menggunakan indeks
print("Item pada indeks 0:", things[0])  # Mengakses item pada indeks 0
print("Item pada indeks 1:", things[1])  # Mengakses item pada indeks 1
print("Item pada indeks 2:", things[2])  # Mengakses item pada indeks 2
print("Item pada indeks 3:", things[3])  # Mengakses item pada indeks 3
print("Item pada indeks 4:", things[4])  # Mengakses item pada indeks 4
print()
# ===============================================================================================
# Syntax List
# Mendefinisikan list listContoh dengan beberapa elemen
listContoh = ["hello", 1, 1, 3, True]

# Menampilkan seluruh isi list
print("Isi dari listContoh:", listContoh)

# Mengakses elemen di setiap indeks dalam list
print("Item pada indeks 0:", listContoh[0])  # Mengakses item pada indeks 0
print("Item pada indeks 1:", listContoh[1])  # Mengakses item pada indeks 1
print("Item pada indeks 2:", listContoh[2])  # Mengakses item pada indeks 2
print("Item pada indeks 3:", listContoh[3])  # Mengakses item pada indeks 3
print("Item pada indeks 4:", listContoh[4])  # Mengakses item pada indeks 4
print()
# ===============================================================================================
# Access Data
# Mendefinisikan list listContoh dengan beberapa elemen
listContoh = ["hello", 1, 1, 3, True]

# Mengakses dan mencetak elemen tertentu berdasarkan indeksnya
print(listContoh[0])  # Mengakses elemen pada indeks 0
print(listContoh[2])  # Mengakses elemen pada indeks 2
print(listContoh[4])  # Mengakses elemen pada indeks 4
print()
# ===============================================================================================
# Access Data Negative Indexing
# Mendefinisikan list listContoh
listContoh = ["hello", 1, 1, 3, True]

# Mengakses elemen menggunakan negative indexing
print(listContoh[-1])  # Mengakses elemen terakhir
print(listContoh[-2])  # Mengakses elemen kedua dari belakang
print(listContoh[-5])  # Mengakses elemen pertama (indeks -5)
print()
# ===============================================================================================
# Access Data Range of Indexes
# Mendefinisikan list listContoh
listContoh = ["hello", 1, 1, 3, True]

# Mengakses elemen dengan range of indexes
print(listContoh[-4:-1])  # Output: [1, 1, 3]
print(listContoh[1:4])    # Output: [1, 1, 3]
print(listContoh[-5:2])   # Output: ['hello', 1]
print(listContoh[0:-2])   # Output: ['hello', 1, 1]
print(listContoh[2:])     # Output: [1, 3, True]
print()
# ===============================================================================================
# Change Data
# Mendefinisikan listContoh
listContoh = ["hello", 1, 1, 3, True]

# Mengubah elemen pada indeks tertentu
listContoh[1] = "test"   # Mengubah elemen pada indeks 1 menjadi 'test'
listContoh[-2] = "coba"  # Mengubah elemen pada indeks -2 (indeks ke-3 dari belakang) menjadi 'coba'

# Menampilkan listContoh setelah perubahan
print(listContoh)  # Output: ['hello', 'test', 1, 'coba', True]
print()
# ===============================================================================================
# Add Data
# Mendefinisikan listContoh
listContoh = ["hello", 1, 1, 3, True]

# Menambahkan elemen 'coba' di akhir list
listContoh.append("coba")

# Menyisipkan elemen 'boleh' pada indeks 1
listContoh.insert(1, "boleh")

# Menampilkan listContoh setelah perubahan
print(listContoh)  # Output: ['hello', 'boleh', 1, 1, 3, True, 'coba']
print()
# ===============================================================================================
# Delete Data
# Mendefinisikan listContoh
listContoh = ["hello", "coba", "coba", 3, True]

# Menghapus elemen pertama yang memiliki nilai 'coba'
listContoh.remove("coba")  # Hanya menghapus elemen "coba" pertama yang ditemukan

# Menghapus elemen terakhir dalam list
listContoh.pop()

# Menghapus elemen pada indeks 1
del listContoh[1]

# Menampilkan listContoh setelah beberapa elemen dihapus
print(listContoh)  # Output: ['hello', 3]

# Menghapus semua elemen dari list
listContoh.clear()

# Menampilkan listContoh setelah dikosongkan
print(listContoh)  # Output: []
# ===============================================================================================
# Loop Through a List
# Mendefinisikan listContoh
listContoh = ["hello", 1, 1, 3, True]

# Melakukan perulangan untuk setiap item di dalam listContoh
for item in listContoh:
    print(item)  # Menampilkan item
print()
# ===============================================================================================
# Check if an Item Exists in a List
# Mendefinisikan listContoh
listContoh = ["hello", 1, 1, 3, True]

# Memeriksa apakah "hello" ada di dalam listContoh
if "hello" in listContoh:
    print("Ada string hello di listContoh")  # Menampilkan pesan jika "hello" ditemukan
else:
    print("string hello tidak ditemukan di listContoh")  # Menampilkan pesan jika "hello" tidak ditemukan
print()
# ===============================================================================================
# Length of List
# Mendefinisikan listContoh
listContoh = ["hello", 1, 1, 3, True]

# Menggunakan fungsi len() untuk mendapatkan panjang list
print(len(listContoh))  # Output: 5
print()
# ===============================================================================================
# Copy a List
# List asli
listContoh = ["hello", "coba", "coba", 3, True]

# Shallow copy (menggunakan assignment)
newList1 = listContoh
newList1[1] = "test"  # Mengubah elemen pada index 1 di newList1

# Copy list menggunakan metode copy() untuk membuat duplikat baru
newList2 = listContoh.copy()
newList2[2] = "baru"  # Mengubah elemen pada index 2 di newList2

# Menampilkan hasil
print(newList1)     # Output: ['hello', 'test', 'coba', 3, True]
print(newList2)     # Output: ['hello', 'test', 'baru', 3, True]
print(listContoh)   # Output: ['hello', 'test', 'coba', 3, True]
print()
# ===============================================================================================
# List Concatenating
# List yang akan digabungkan
listContoh = ["hello", "coba", "coba", 3, True]
listBaru = [5, "test", False]
listCoba = ["tarik", 8]

# Menggabungkan listBaru dan listContoh menggunakan operasi +
listGabungan = listBaru + listContoh
print(listGabungan)  # Output: [5, 'test', False, 'hello', 'coba', 'coba', 3, True]

# Menggabungkan listGabungan dengan listCoba menggunakan metode .extend()
listGabungan.extend(listCoba)
print(listGabungan)  # Output: [5, 'test', False, 'hello', 'coba', 'coba', 3, True, 'tarik', 8]
print()
# ===============================================================================================
# Find Index
# List yang berisi beberapa nama
# listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
#
# # Mencari indeks dari elemen 'andi' dalam list
# indexYgDicari1 = listContoh.index('andi')
# print(indexYgDicari1)  # Output: 2
#
# # Mencari indeks dari elemen 'bernard' dalam list
# # Ini akan menghasilkan error karena 'bernard' tidak ada dalam list
# indexYgDicari2 = listContoh.index('bernard')
# print(indexYgDicari2)
# print()
# ===============================================================================================
# Sorting
# List yang berisi beberapa nama
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']

# Mengurutkan elemen dalam list secara alfabetis
listContoh.sort()

# Menampilkan list yang sudah diurutkan
print(listContoh)  # Output: ['andi', 'baron', 'charlie', 'eddie', 'samson']

# ===============================================================================================
# Reverse
# List yang berisi beberapa nama
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']

# Membalikkan urutan elemen dalam list
listContoh.reverse()

# Menampilkan list yang sudah dibalik
print(listContoh)  # Output: ['samson', 'charlie', 'andi', 'baron', 'eddie']

# ===============================================================================================
# 2D List
# List satu dimensi (One Dimension)
list_satu_dimensi = ["Buku", "Pulpen Biru", "Majalah", "Laptop", "Pulpen Merah"]

# Menampilkan seluruh isi list satu dimensi
print("List Satu Dimensi:")
for item in list_satu_dimensi:
    print(item)

# List dua dimensi (Two Dimensions)
list_dua_dimensi = [
    ["Pulpen Merah", "Pulpen Biru"],       # Baris pertama
    ["Jam Dinding", "Jam Digital"],        # Baris kedua
    ["Sepatu Futsal", "Sepatu Olahraga"]   # Baris ketiga
]

# Menampilkan seluruh isi list dua dimensi
print("\nList Dua Dimensi:")
for baris in list_dua_dimensi:
    for item in baris:
        print(item)

# ===============================================================================================
# 2D List (2)
# Mendefinisikan list dua dimensi
things = [
    ["red pen", "blue pen"],
    ["analog clock", "digital clock"],
    ["futsal shoes", "badminton shoes"]
]

# Menampilkan list dua dimensi sebelum perubahan
print("List sebelum perubahan:")
for row in things:
    print(row)

# Mengubah elemen pada indeks ke-2 (baris ketiga)
things[2] = ["futsal shoes", "badminton shoes"]

# Mengubah elemen pada indeks ke-2 dan sub-indeks ke-1 (baris ketiga, kolom kedua)
things[2][1] = "badminton shoes"

# Menampilkan list dua dimensi setelah perubahan
print("\nList setelah perubahan:")
for row in things:
    print(row)
print()
# ===============================================================================================
#



