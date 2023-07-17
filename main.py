
def level18():
    hasil = []
    kata = input("masukkan kata anda: ")
    kata = kata.lower().split()

    for i in kata:
        balik_kata = i[::-1]
        hasil.append(balik_kata)

    join_kata = ' '.join(hasil)
    print(join_kata)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level18()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
