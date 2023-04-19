import sys


def main(infile):
    with open(infile, 'r') as file:
        text_file = file.read()

    letter_count = len(text_file)
    letter_dictionary = {}

    for letter in text_file:
        if letter.lower() not in letter_dictionary.keys():
            letter_dictionary[letter.lower()] = 1
        else:
            letter_dictionary[letter.lower()] += 1

    for letter in letter_dictionary:
        letter_dictionary[letter] = round(letter_dictionary[letter]/letter_count, 3)

    print(letter_dictionary)


if __name__ == '__main__':
    main(sys.argv[1])