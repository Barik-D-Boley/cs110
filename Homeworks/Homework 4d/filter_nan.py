import sys


def main(infile, outfile):
    new_file = []

    with open(infile, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            if line != 'NaN':
                new_file.append(line)

    with open(outfile, 'w') as file:
        file.writelines('\n'.join(new_file))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])