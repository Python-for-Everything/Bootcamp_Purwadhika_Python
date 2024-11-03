"""Exercise Module 1 Day 6"""
# Soal 1a
# Bentuk 1 - Garis Horizontal

print("Garis Horizontal:")
for i in range(5):
    print("*", end=" ")
print("\n")

# ===============================================================================================
# Soal 1b
# Bentuk 2 - Garis Vertikal

print("Garis Vertikal:")
for i in range(5):
    print("*")
# ===============================================================================================
# Soal 1c
# Bentuk 3 - Garis Persegi
print("\nPersegi:")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# ===============================================================================================
# Soal 1d
# Bentuk 4 - Garis Segitiga
print("\nSegitiga:")
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
# ===============================================================================================
# Soal 2
stars = ''

for i in range(5):
    stars += '* '
print(stars)

# ===============================================================================================
# Soal 3
print("\nstars")
stars = ''

# Loop sebanyak 5 kali
for i in range(5):
    stars += '*\n'
# Cetak hasil
print(stars)
# ===============================================================================================
# Soal 4
stars = ''
size = 5

for i in range(size):
    for j in range(size):
        stars += '* '
    stars += '\n'
print(stars)

# ===============================================================================================
# Soal 5
stars = ''
size = 5

for i in range(size):
    for j in range(1 + i):
        stars += '* '
    stars += '\n'
print(stars)

# ===============================================================================================
#