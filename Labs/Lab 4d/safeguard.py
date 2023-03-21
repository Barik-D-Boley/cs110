import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()


def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)


def main(infile, outfile):
    lines = readlines(infile)

    writelines(outfile, lines)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
