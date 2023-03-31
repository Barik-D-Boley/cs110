import sys
import re


def main(infile, outfile, zipcode_map):
    new_file = []

    with open(infile, 'r') as file:
        for line in file:
            new_file.append('unknown\n')
            for zipcode in zipcode_map:
                if re.search(str(zipcode), line):
                    new_file.pop()
                    new_file.append(f'{str(zipcode_map[zipcode])}\n')

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    zip_code_to_delivery_bin = {
        5208: 16,
        10118: 4,
        227: 76,
        12345: 1,
        84604: 25,
        84602: 25,
        20895: 82
    }
    main(sys.argv[1], sys.argv[2], zip_code_to_delivery_bin)