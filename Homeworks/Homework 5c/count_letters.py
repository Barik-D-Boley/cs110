import sys


def main(string, infile):
    letters = {}

    with open(infile, 'r') as file:
        file_read = file.read()

    for letter in string:
        if not letter in letters.keys():
            letters[letter] = 0

    for letter in file_read:
        if letter.lower() in letters.keys():
            letters[letter.lower()] += 1

    print(letters)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])