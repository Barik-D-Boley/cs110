import sys, random


def main(outfile):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = random.sample(alphabet, len(alphabet))

    with open(outfile, 'w') as file:
        file.writelines('')

    for i, letter in enumerate(alphabet):
        with open(outfile, 'a') as file:
            if i != len(alphabet)-1:
                file.writelines(f'{letter},{cipher[i]}\n')
            else:
                file.writelines(f'{letter},{cipher[i]}')


if __name__ == '__main__':
    main(sys.argv[1])