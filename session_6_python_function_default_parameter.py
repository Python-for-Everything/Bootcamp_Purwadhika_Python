# Definisi fungsi dengan default parameter
def salamBalik(nama="Unknown", usia=0):
    # Memeriksa kondisi berdasarkan nilai nama dan usia
    if nama == "Unknown" and usia > 0:
        print("Saya berusia {}".format(usia))
    elif nama != "Unknown" and usia == 0:
        print("Hello nama saya {}".format(nama))
    elif nama != "Unknown" and usia > 0:
        print("Hello perkenalkan nama saya {}, dan usia saya {}".format(nama, usia))

    # Pesan tambahan
    print("Senang bertemu dengan anda!")


# Memanggil fungsi dengan berbagai kombinasi argument
salamBalik(usia=25)
salamBalik("Budi")
salamBalik(nama="Andi", usia=21)
