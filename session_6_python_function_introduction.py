# ==============================================================================================
# Soal 1
# Masukkan 5 Film kesukaan anda di pisah dengan koma : Avengers,Hulk,Iron Man 3, Wonder Woman, Batman

# Masukkan 5 Film kesukaan teman anda dipisahkan dengan koma : Avengers,Hulk,Iron Man 2, Superman,
# Wonder Woman.

# Kesukaan Film kalian yang sama sebesar 60.0%

# Meminta input 5 film kesukaan pengguna
film_saya = input("Masukkan 5 Film kesukaan anda dipisahkan dengan koma: ").split(',')

# Meminta input 5 film kesukaan teman pengguna
film_teman = input("Masukkan 5 Film kesukaan teman anda dipisahkan dengan koma: ").split(',')

# Mengubah list film menjadi set untuk menemukan irisan (intersection)
set_film_saya = set(film_saya)
set_film_teman = set(film_teman)

# Menghitung film yang sama dengan menggunakan intersection
film_sama = set_film_saya.intersection(set_film_teman)

# Menghitung persentase kesamaan
persentase_kesamaan = (len(film_sama) / 5) * 100

# Menampilkan hasil
print(f"Kesukaan Film kalian yang sama sebesar {persentase_kesamaan}%")
print()
