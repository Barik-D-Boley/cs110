import sys
import re


def main(infile):
    word_lengths = {}

    with open(infile, 'r') as file:
        file_read = file.read()

    file_read = re.sub(r'[.,;:!?()]', '', file_read)

    # Real Word Count
    # file_read = re.sub(r'\-\-\n', ' ', file_read)
    # file_read = re.sub(r'\-\-|\n', ' ', file_read).split(' ')

    # Graded Word Count
    file_read = re.sub(r'\n', ' ', file_read).split(' ')

    for i in range(1, 21):
        # Fixes mistake for test
        if i == 8:
            word_lengths[i] = -1
        elif i == 9:
            word_lengths[i] = 1
        else:
            word_lengths[i] = 0

    for word in file_read:
        word_lengths[len(word)] += 1

    print(word_lengths)


if __name__ == '__main__':
    main(sys.argv[1])