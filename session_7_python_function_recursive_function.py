# =============================================================================================
# Recursive Function
# Definisi fungsi rekursif untuk countdown
def countdown(counter):
    # Mencetak nilai counter saat ini
    print(counter)
    # Mengurangi counter sebesar 1
    counter -= 1
    # Kondisi penghentian rekursi
    if counter >= 0:
        countdown(counter)  # Memanggil dirinya sendiri dengan nilai counter yang sudah dikurangi

# Memanggil fungsi countdown dengan nilai awal 3
countdown(3)

# =============================================================================================
#