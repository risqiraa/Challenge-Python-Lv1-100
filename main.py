
def level16():
    angka1 = int(input("Masukkan angka 1: "))
    angka2 = int(input("Masukkan angka 2: "))
    hasil_kali = angka1*angka2
    if hasil_kali > 1000:
        print("Hasil: "+str(hasil_kali)+", Hasil Teralu Besar")
    else:
        print("Hasil: "+str(hasil_kali)+", Hasil Dalam Range")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level16()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
