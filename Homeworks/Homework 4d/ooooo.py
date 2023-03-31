import sys
import re


def main(infile, outfile):
    new_file = None

    with open(infile, 'r') as file:
        new_file = re.sub('[aeiouAEIOU]', 'o', file.read())

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])