import sys, re


def main(cipher_file, infile, outfile):
    with open(cipher_file, 'r') as file:
        cipher = file.read()

    with open(infile, 'r') as file:
        encoded_text = file.read()

    cipher = cipher.split('\n')
    cipher_dictionary = {}
    decoded_text = []

    for line in cipher:
        if not re.match(r'[a-zA-Z],[a-zA-Z]', line):
            return
        cipher_dictionary[line.split(',')[1]] = line.split(',')[0]

    for letter in encoded_text:
        if letter.lower() in cipher_dictionary.keys() and letter.islower():
            decoded_text.append(cipher_dictionary[letter])
        elif letter.lower() in cipher_dictionary.keys() and letter.isupper():
            decoded_text.append(cipher_dictionary[letter.lower()].upper())
        else:
            decoded_text.append(letter)

    with open(outfile, 'w') as file:
        file.writelines(''.join(decoded_text))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])