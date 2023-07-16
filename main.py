def level8():
    angka1 = input("input susunan angka1 (pisahkan dengan koma): ")
    angka2 = input("input susunan angka2 (pisahkan dengan koma): ")
    listAngka1 = angka1.split(",")
    listAngka2 = angka2.split(",")
    listAngka1 = [int(angka) for angka in listAngka1]
    listAngka2 = [int(angka) for angka in listAngka2]
    gabungan = sorted(list(set(listAngka1+listAngka2)))

    print("List angka1: "+str(listAngka1))
    print("List angka2: "+str(listAngka2))
    print("Gabungan 2 Susunan angka tersebut adalah: "+str(gabungan))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level8()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
