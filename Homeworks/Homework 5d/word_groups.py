import sys
import re


def main(infile):
    word_types = []
    reduced_word_types = []

    with open(infile, 'r') as file:
        file_read = str(file.readlines())
        file_read = re.sub(r'\\n|[^\w\s]', '', file_read).split()

    for word in file_read:
        word = word.lower()
        word_types.append((len(word), word[0]))

    for word_type in word_types:
        if word_type not in reduced_word_types:
            reduced_word_types.append(word_type)

    for word_type in reduced_word_types:
        print(f'{word_type}: {[x.lower() for x in file_read if len(x) == word_type[0] and x[0].lower() == word_type[1]]}')


if __name__ == '__main__':
    main(sys.argv[1])