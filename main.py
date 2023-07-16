
def level15():
    hasil_f=[0,1]
    A1, A2 = 0,1
    max_angka = int(input("masukkan maksimal angka: "))
    while A2 <= max_angka:
        A1,A2 = A2, A1+A2
        if A2 >= max_angka:
            break
        hasil_f.append(A2)

    print(hasil_f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level15()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
