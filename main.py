
def level11():
    hitung_vokal = 0
    hitung_konsonan = 0
    kata = input("masukkan kata anda: ")
    kata = list(kata.lower())
    print (kata)
    for huruf in kata:
        if huruf.lower() in ["a","i","u","e","o"]:
            hitung_vokal +=1
        else:
            hitung_konsonan +=1

    print("Vokal: "+str(hitung_vokal)+"\nKonsonan: "+str(hitung_konsonan))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level11()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
