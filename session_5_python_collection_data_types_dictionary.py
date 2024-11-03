# ============================================================================================
# Dictionary Introduction
# Mendefinisikan dictionary 'things' dengan kunci dan nilai
things = {
    0: "book",            # Kunci 0 untuk item "book"
    1: "blue pen",        # Kunci 1 untuk item "blue pen"
    2: "photo album",     # Kunci 2 untuk item "photo album"
    3: "laptop",          # Kunci 3 untuk item "laptop"
    4: "red pen"          # Kunci 4 untuk item "red pen"
}

# Menampilkan isi dari dictionary 'things'
print("Isi dictionary 'things':", things)

# Mengakses item tertentu berdasarkan kunci
print("Item dengan kunci 0:", things[0])  # Mengakses item "book"
print("Item dengan kunci 1:", things[1])  # Mengakses item "blue pen"
print("Item dengan kunci 2:", things[2])  # Mengakses item "photo album"
print("Item dengan kunci 3:", things[3])  # Mengakses item "laptop"
print("Item dengan kunci 4:", things[4])  # Mengakses item "red pen"
print()
# ============================================================================================
# Dictionary Introduction (2)
# Mendefinisikan dictionary 'things' dengan nama kunci dalam bahasa Indonesia
things = {
    "buku": "gambar buku",             # Kunci 'buku' untuk item "gambar buku"
    "pulpenbiru": "gambar pulpen biru", # Kunci 'pulpenbiru' untuk item "gambar pulpen biru"
    "photoalbum": "gambar photo album", # Kunci 'photoalbum' untuk item "gambar photo album"
    "laptop": "gambar laptop",          # Kunci 'laptop' untuk item "gambar laptop"
    "pulpenmerah": "gambar pulpen merah" # Kunci 'pulpenmerah' untuk item "gambar pulpen merah"
}

# Menampilkan isi dari dictionary 'things'
print("Isi dictionary 'things':", things)

# Mengakses item tertentu berdasarkan kunci
print("Item dengan kunci 'buku':", things["buku"])           # Mengakses item "gambar buku"
print("Item dengan kunci 'pulpenbiru':", things["pulpenbiru"]) # Mengakses item "gambar pulpen biru"
print("Item dengan kunci 'photoalbum':", things["photoalbum"]) # Mengakses item "gambar photo album"
print("Item dengan kunci 'laptop':", things["laptop"])         # Mengakses item "gambar laptop"
print("Item dengan kunci 'pulpenmerah':", things["pulpenmerah"]) # Mengakses item "gambar pulpen merah"
print()
# ============================================================================================
# Dictionary Introduction (3)
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',         # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,             # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False        # Kunci 'menikah' dengan nilai False
}

# Menampilkan isi dari dictionary 'dictionaryContoh'
print("Isi dictionary 'dictionaryContoh':", dictionaryContoh)

# Mengakses setiap item berdasarkan kunci
print("Nama:", dictionaryContoh['nama'])         # Mengakses nilai dari kunci 'nama'
print("Usia:", dictionaryContoh['usia'])         # Mengakses nilai dari kunci 'usia'
print("Pekerjaan:", dictionaryContoh['pekerjaan']) # Mengakses nilai dari kunci 'pekerjaan'
print("Menikah:", dictionaryContoh['menikah'])     # Mengakses nilai dari kunci 'menikah'
print()
# ============================================================================================
# Syntax Dictionary
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',         # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,             # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False        # Kunci 'menikah' dengan nilai False
}

# Menampilkan isi dari dictionary 'dictionaryContoh'
print("Isi dictionary 'dictionaryContoh':", dictionaryContoh)

# Mengakses setiap item berdasarkan kunci
print("Nama:", dictionaryContoh['nama'])         # Mengakses nilai dari kunci 'nama'
print("Usia:", dictionaryContoh['usia'])         # Mengakses nilai dari kunci 'usia'
print("Pekerjaan:", dictionaryContoh['pekerjaan']) # Mengakses nilai dari kunci 'pekerjaan'
print("Menikah:", dictionaryContoh['menikah'])     # Mengakses nilai dari kunci 'menikah'
print()
# ============================================================================================
# Create Dictionary
# Cara 1: Membuat dictionary menggunakan kurung kurawal {}
dictionaryContoh1 = {
    'nama': 'Budi',         # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,             # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer' # Kunci 'pekerjaan' dengan nilai 'Developer'
}

# Menampilkan isi dari dictionaryContoh1
print("Isi dictionaryContoh1:", dictionaryContoh1)  # Output: {'nama': 'Budi', 'usia': 25, 'pekerjaan': 'Developer'}

# Cara 2: Membuat dictionary menggunakan fungsi dict()
dictionaryContoh2 = dict(nama='Andi', usia=27, pekerjaan='Data Scientist')

# Menampilkan isi dari dictionaryContoh2
print("Isi dictionaryContoh2:", dictionaryContoh2)  # Output: {'nama': 'Andi', 'usia': 27, 'pekerjaan': 'Data Scientist'}
print()
# ============================================================================================
# Access Data
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Mengakses nilai dalam dictionary menggunakan kunci secara langsung
print(dictionaryContoh['nama'])     # Output: Budi
print(dictionaryContoh['usia'])     # Output: 25

# Mengakses nilai dalam dictionary menggunakan metode .get()
print(dictionaryContoh.get('pekerjaan')) # Output: Developer
print(dictionaryContoh.get('menikah'))   # Output: False
print()
# ============================================================================================
# Change Data
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Mengubah nilai pada kunci 'usia' menjadi 27
dictionaryContoh['usia'] = 27

# Menampilkan isi dari dictionary setelah perubahan
print(dictionaryContoh)  # Output: {'nama': 'Budi', 'usia': 27, 'pekerjaan': 'Developer', 'menikah': False}
print()
# ============================================================================================
# Add Data
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Menambahkan data baru ke dictionary dengan kunci 'kelamin' dan nilai 'Pria'
dictionaryContoh['kelamin'] = 'Pria'

# Menampilkan isi dari dictionary setelah penambahan data baru
print(dictionaryContoh)  # Output: {'nama': 'Budi', 'usia': 25, 'pekerjaan': 'Developer', 'menikah': False, 'kelamin': 'Pria'}
print()
# ============================================================================================
# Delete Data
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False,        # Kunci 'menikah' dengan nilai False
    'kelamin': 'Pria'        # Kunci 'kelamin' dengan nilai 'Pria'
}

# Menghapus item berdasarkan kunci menggunakan 'del'
del dictionaryContoh['kelamin']  # Menghapus pasangan kunci-nilai dengan kunci 'kelamin'

# Menghapus item berdasarkan kunci menggunakan 'pop'
dictionaryContoh.pop('usia')     # Menghapus pasangan kunci-nilai dengan kunci 'usia'

# Menghapus item terakhir yang dimasukkan menggunakan 'popitem'
dictionaryContoh.popitem()       # Menghapus item terakhir yang dimasukkan dalam dictionary

# Menampilkan isi dari dictionary setelah beberapa item dihapus
print(dictionaryContoh)  # Output: {'nama': 'Budi', 'pekerjaan': 'Developer'}

# Menghapus semua item dari dictionary menggunakan 'clear'
dictionaryContoh.clear()         # Mengosongkan seluruh isi dictionary

# Menampilkan isi dari dictionary setelah dikosongkan
print(dictionaryContoh)  # Output: {}
print()
# ============================================================================================
# Loop Through a Dictionary
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Loop melalui dictionary untuk mengakses kunci dan nilai
for key in dictionaryContoh:
    print("{} = {}".format(key, dictionaryContoh[key]))

# Loop melalui dictionary menggunakan .keys() untuk mengakses kunci dan nilai
for key in dictionaryContoh.keys():
    print("{} = {}".format(key, dictionaryContoh[key]))

# Loop melalui dictionary menggunakan .values() untuk mengakses hanya nilai
for val in dictionaryContoh.values():
    print(val)

# Loop melalui dictionary menggunakan .items() untuk mengakses kunci dan nilai secara langsung
for key, val in dictionaryContoh.items():
    print("{} = {}".format(key, val))
print()
# ============================================================================================
# Check if a Key Exist in a Dictionary
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Memeriksa apakah kunci 'usia' ada di dalam dictionary
if 'usia' in dictionaryContoh:
    print('Ada key usia pada dictionaryContoh')
else:
    print('Tidak ada key usia pada dictionaryContoh')
print()
# ============================================================================================
# Length of Dictionary
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Menghitung jumlah item di dalam dictionary
print(len(dictionaryContoh))  # Output: 4
print()
# ============================================================================================
# Copy a Dictionary
# Mendefinisikan dictionary 'dictionaryContoh' dengan beberapa pasangan kunci-nilai
dictionaryContoh = {
    'nama': 'Budi',          # Kunci 'nama' dengan nilai 'Budi'
    'usia': 25,              # Kunci 'usia' dengan nilai 25
    'pekerjaan': 'Developer', # Kunci 'pekerjaan' dengan nilai 'Developer'
    'menikah': False         # Kunci 'menikah' dengan nilai False
}

# Membuat salinan dictionary dengan referensi langsung
newDictionary1 = dictionaryContoh
newDictionary1['nama'] = 'Andi'  # Mengubah nilai 'nama' pada newDictionary1

# Membuat salinan dictionary dengan metode copy()
newDictionary2 = dictionaryContoh.copy()
newDictionary2['pekerjaan'] = 'Guru'  # Mengubah nilai 'pekerjaan' pada newDictionary2

# Menampilkan isi dari setiap dictionary
print("newDictionary1:", newDictionary1)      # Output: {'nama': 'Andi', 'usia': 25, 'pekerjaan': 'Developer', 'menikah': False}
print("newDictionary2:", newDictionary2)      # Output: {'nama': 'Andi', 'usia': 25, 'pekerjaan': 'Guru', 'menikah': False}
print("dictionaryContoh:", dictionaryContoh)  # Output: {'nama': 'Andi', 'usia': 25, 'pekerjaan': 'Developer', 'menikah': False}
print()
# ============================================================================================
# Dictionary inside Dictionary
# Mendefinisikan dictionary 'things' yang berisi dictionary lain di dalamnya
things = {
    'food1': {
        'name': 'Ramen',
        'price': 25000
    },
    'food2': {
        'name': 'Pizza',
        'price': 30000
    },
    'food3': {
        'name': 'Spaghetti',
        'price': 20000
    }
}

# Mengakses dictionary di dalam dictionary
print("things['food1']:", things['food1'])  # Output: {'name': 'Ramen', 'price': 25000}
print("things['food2']['name']:", things['food2']['name'])  # Output: Pizza
print()
# ============================================================================================














