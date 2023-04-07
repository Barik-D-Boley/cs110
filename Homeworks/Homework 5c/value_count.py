import sys
import re


def main(infile, column):
    values = {}

    with open(infile, 'r') as file:
        file_read = file.readlines()

    for i, line in enumerate(file_read):
        line = re.sub('\\n', '', line).split(',')

        if not line[int(column)] in values.keys():
            values[line[int(column)]] = 1
        else:
            values[line[int(column)]] += 1

    print(values)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])