
def level14():
    jumlah_kata = 0
    kata = input("masukkan kalimat anda: ")
    set_kata = set(kata.lower().split())
    print(set_kata)
    for i in set_kata:
        if len(i) == 3:
            jumlah_kata +=1

    print("Jumlah Kata 3huruf: "+str(jumlah_kata))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level14()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
