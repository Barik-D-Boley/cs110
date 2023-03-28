import sys
import re


def main(infile, outfile, old_word, new_word):
    with open(infile, 'r') as file:
        new_file = re.sub(old_word, new_word, file.read())

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])