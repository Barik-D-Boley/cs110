def main():
    word_list = []
    short_words = []

    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            word_list.append(word)

    word_length = int(input('Enter a length: '))

    for i in range(len(word_list)):
        if len(word_list[i]) <= word_length:
            short_words.append(word_list[i])

    print(f'There are {len(short_words)} short words:')

    for i in range(len(short_words)):
        print(f'- {short_words[i]}')


if __name__ == '__main__':
    main()
