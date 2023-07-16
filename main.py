
def level13():
    kata = input("masukkan kata anda: ")
    kata_unik = len(set(kata.lower().split()))
    print("Jumlah Kata Unik: "+str(kata_unik))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level13()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
