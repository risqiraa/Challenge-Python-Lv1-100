from collections import Counter
def level9():
    word = input("Masukkan kalimat anda: ")
    word = word.lower().split()
    word_count = Counter(word)
    word_count1 = word_count.most_common(2)
    print(word_count)
    print(word_count1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level9()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
