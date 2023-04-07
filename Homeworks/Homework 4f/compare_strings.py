def main():
    while True:
        compare = []

        first_word = input('Word 1: ')
        if first_word == '':
            break
        second_word = input('Word 2: ')

        for i, letter in enumerate(first_word):
            if letter == second_word[i]:
                compare.append('*')
            else:
                compare.append('.')

        print(''.join(compare))


if __name__ == '__main__':
    main()