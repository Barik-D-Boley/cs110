import sys


def main(min_length):
    word_list = []

    while True:
        word = input('Word: ')
        if len(word) < int(min_length):
            print('Too short.')
        else:
            word_list.append(word)

        if len(word_list) == 5:
            break

    for i in range(len(word_list)):
        print(f'- {word_list[i]}')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("This program takes one argument, a superlative.")
        print("For example: 'stupendous' or 'fantastic'")
        exit()

    superlative = sys.argv[1]
    main(superlative)