import sys, re


def main(cipher_file, infile, outfile):
    with open(cipher_file, 'r') as file:
        cipher = file.read()

    with open(infile, 'r') as file:
        plain_text = file.read()

    cipher = cipher.split('\n')
    cipher_dictionary = {}
    encoded_text = []

    for line in cipher:
        if re.match(r'[a-zA-Z],[a-zA-Z]', line):
            cipher_dictionary[line.split(',')[0]] = line.split(',')[1]

    for letter in plain_text:
        if letter.lower() in cipher_dictionary.keys() and letter.islower():
            encoded_text.append(cipher_dictionary[letter])
        elif letter.lower() in cipher_dictionary.keys() and letter.isupper():
            encoded_text.append(cipher_dictionary[letter.lower()].upper())
        else:
            encoded_text.append(letter)

    with open(outfile, 'w') as file:
        file.writelines(''.join(encoded_text))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])