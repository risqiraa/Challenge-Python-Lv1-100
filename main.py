def level6():

    angka1 = input("masukkan angka ke-1: ")
    angka2 = input("masukkan angka ke-2: ")
    angka1 = int(angka1)
    angka2 = int(angka2)
    numbers = []
    for number in range(angka1, angka2 + 1):
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                numbers.append(number)

    print("Bilangan Prima Antara " + str(angka1) + " dan " + str(angka2) + " adalah: " + str(numbers))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
