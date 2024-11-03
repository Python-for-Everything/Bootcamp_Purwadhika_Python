# ===============================================================================================
# Syntax Set
# Mendefinisikan sebuah set dengan beberapa elemen
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Iron Man 3'}

# Menampilkan isi dari set
print(setContoh)
print()
# ===============================================================================================
# Create Set from List, Tuple, and Dictionary
# Membuat set dari list
list1 = ['Budi', 2, 2, 'Ceci']
setList = set(list1)
print("Set dari list:", setList)  # Output yang mungkin: {'Ceci', 2, 'Budi'}

# Membuat set dari tuple
tuple1 = (False, 1, 'Andi', False)
setTuple = set(tuple1)
print("Set dari tuple:", setTuple)  # Output yang mungkin: {False, 1, 'Andi'}

# Membuat set dari dictionary
dictionary1 = {
    'nama': 'Coder',
    'usia': 25,
    'pekerjaan': 'Coder',
    'menikah': False
}
setDictionary = set(dictionary1)
print("Set dari keys dictionary:", setDictionary)  # Output yang mungkin: {'nama', 'usia', 'pekerjaan', 'menikah'}

# Membuat set dari nilai (values) dictionary
setDictionaryValues = set(dictionary1.values())
print("Set dari values dictionary:", setDictionaryValues)  # Output yang mungkin: {'Coder', False, 25}
print()
# ===============================================================================================
# Access Data
# Mendefinisikan sebuah set dengan beberapa elemen unik
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

# Mengakses dan mencetak setiap item dalam set
for item in setContoh:
    print(item)
print()
# ===============================================================================================
# Check if an Item Exists in a Set
# Mendefinisikan sebuah set dengan beberapa elemen unik
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

# Memeriksa apakah 'Iron Man 3' ada di dalam set
if 'Iron Man 3' in setContoh:
    print('Ada film Iron Man 3 pada setContoh')
else:
    print('Tidak ada film Iron Man 3 pada setContoh')
print()
# ===============================================================================================
# Add Data
# Mendefinisikan sebuah set dengan beberapa elemen unik
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

# Menambahkan satu elemen baru ke dalam set menggunakan add()
setContoh.add('Iron Man')
print("Set setelah menggunakan add():", setContoh)
# Output yang mungkin: {'Avengers: Age of Ultron', 'The Avengers', 'Iron Man 3', 'Iron Man'}

# Menambahkan beberapa elemen baru ke dalam set menggunakan update()
setContoh.update({'Iron Man 3', 'Hulk'})
print("Set setelah menggunakan update():", setContoh)
# Output yang mungkin: {'Hulk', 'Iron Man 3', 'Avengers: Age of Ultron', 'The Avengers', 'Iron Man'}
print()
# ===============================================================================================
# Delete Data
# Mendefinisikan sebuah set dengan beberapa elemen unik
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk', 'Wonder Woman'}

# Menghapus elemen tertentu menggunakan remove()
setContoh.remove('The Avengers')
print("Set setelah menggunakan remove('The Avengers'):", setContoh)
# Output yang mungkin: {'Wonder Woman', 'Hulk', 'Iron Man 3', 'Avengers: Age of Ultron'}

# Menghapus elemen tertentu menggunakan discard()
setContoh.discard('Hulk')
print("Set setelah menggunakan discard('Hulk'):", setContoh)
# Output yang mungkin: {'Wonder Woman', 'Iron Man 3', 'Avengers: Age of Ultron'}

# Menghapus elemen secara acak menggunakan pop()
setContoh.pop()
print("Set setelah menggunakan pop():", setContoh)
# Output akan berbeda-beda karena pop() menghapus elemen acak

# Menghapus semua elemen di dalam set menggunakan clear()
setContoh.clear()
print("Set setelah menggunakan clear():", setContoh)
# Output: set()
print()
# ===============================================================================================
# Length of Set
# Mendefinisikan sebuah set dengan beberapa elemen unik
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}

# Menghitung jumlah elemen di dalam set
print(len(setContoh))  # Output: 4
print()
# ===============================================================================================
# Join Sets
# Mendefinisikan dua set dengan beberapa elemen unik
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers'}

# Menggabungkan kedua set menggunakan union()
setGabungan = setMovie1.union(setMovie2)
print("Set Gabungan:", setGabungan)
# Output yang mungkin: {'Iron Man 3', 'Hulk', 'Titanic', 'The Avengers', 'Avengers: Age of Ultron'}
print()
# ===============================================================================================
# Get difference between 2 sets
# Mendefinisikan dua set dengan beberapa elemen unik
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

# Menggunakan metode difference() untuk mendapatkan elemen yang hanya ada di setMovie1
setMovie3 = setMovie1.difference(setMovie2)
print("Set setelah menggunakan difference():", setMovie3)
# Output yang mungkin: {'Avengers: Age of Ultron', 'Iron Man 3'}

# Memeriksa isi setMovie1 untuk memastikan bahwa difference() tidak mengubahnya
print("Isi setMovie1 setelah difference():", setMovie1)
# Output: {'Iron Man 3', 'Hulk', 'The Avengers', 'Avengers: Age of Ultron'}

# Menggunakan metode difference_update() untuk menghapus elemen yang ada di setMovie2 dari setMovie1
setMovie1.difference_update(setMovie2)
print("Set setelah menggunakan difference_update():", setMovie1)
# Output yang mungkin: {'Iron Man 3', 'Avengers: Age of Ultron'}
print()
# ===============================================================================================
# Get symmetric difference between 2 sets
# Mendefinisikan dua set dengan beberapa elemen unik
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

# Menggunakan metode symmetric_difference() untuk mendapatkan elemen yang hanya ada di salah satu set
setMovie3 = setMovie1.symmetric_difference(setMovie2)
print("Set setelah menggunakan symmetric_difference():", setMovie3)
# Output yang mungkin: {'Avengers: Age of Ultron', 'Iron Man 3', 'Titanic'}

# Memeriksa isi setMovie1 untuk memastikan bahwa symmetric_difference() tidak mengubahnya
print("Isi setMovie1 setelah symmetric_difference():", setMovie1)
# Output: {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}

# Menggunakan metode symmetric_difference_update() untuk mengupdate setMovie1 dengan elemen yang hanya ada di salah satu set
setMovie1.symmetric_difference_update(setMovie2)
print("Set setelah menggunakan symmetric_difference_update():", setMovie1)
# Output yang mungkin: {'Iron Man 3', 'Avengers: Age of Ultron', 'Titanic'}
print()
# ===============================================================================================
# Get intersection between 2 sets
# Mendefinisikan dua set dengan beberapa elemen unik
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

# Menggunakan metode intersection() untuk mendapatkan elemen yang ada di kedua set
setMovie3 = setMovie1.intersection(setMovie2)
print("Set setelah menggunakan intersection():", setMovie3)
# Output yang mungkin: {'The Avengers', 'Hulk'}

# Memeriksa isi setMovie1 untuk memastikan bahwa intersection() tidak mengubahnya
print("Isi setMovie1 setelah intersection():", setMovie1)
# Output: {'Iron Man 3', 'The Avengers', 'Avengers: Age of Ultron', 'Hulk'}

# Menggunakan metode intersection_update() untuk memperbarui setMovie1 dengan elemen yang ada di kedua set
setMovie1.intersection_update(setMovie2)
print("Set setelah menggunakan intersection_update():", setMovie1)
# Output yang mungkin: {'The Avengers', 'Hulk'}
print()
# ===============================================================================================
# Check disjoint, subset, and superset
# Mendefinisikan dua set dengan beberapa elemen unik
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'The Avengers', 'Hulk'}

# Memeriksa apakah setMovie1 dan setMovie2 adalah disjoint (tidak memiliki elemen yang sama)
checkDisjoint = setMovie1.isdisjoint(setMovie2)
print("Apakah setMovie1 dan setMovie2 disjoint?", checkDisjoint)
# Output: False (karena mereka memiliki elemen yang sama: 'The Avengers' dan 'Hulk')

# Memeriksa apakah setMovie2 adalah subset dari setMovie1
checkSubset = setMovie2.issubset(setMovie1)
print("Apakah setMovie2 adalah subset dari setMovie1?", checkSubset)
# Output: True (karena semua elemen di setMovie2 ada di setMovie1)

# Memeriksa apakah setMovie1 adalah superset dari setMovie2
checkSuperset = setMovie1.issuperset(setMovie2)
print("Apakah setMovie1 adalah superset dari setMovie2?", checkSuperset)
# Output: True (karena setMovie1 memiliki semua elemen dari setMovie2)
print()
# ===============================================================================================












