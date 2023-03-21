import sys


def main(infile, outfile, bullet):
    new_file = []

    with open(infile, 'r') as file:
        for line in file:
            new_file.append(f'{bullet} {line}')

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])