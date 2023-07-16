def level5():

    numbers = []
    while True:
        angka = input("input angka anda, ketik end jika ingin mengakhiri: ")

        if angka.lower() == "end":
            break

        numbers.append(int(angka))

    print(numbers[::-1])









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level5()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
