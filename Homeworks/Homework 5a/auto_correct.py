import sys
import re


def main(infile, outfile, corrections):
    new_file = []

    with open(infile, 'r') as file:
        for line in file:
            print(line)
            for correction in corrections:
                line = re.sub(rf'\b{str(correction)}\b', str(corrections[correction]), line)
                pass
            new_file.append(line)

    print(new_file)

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    corrections = {
        'teh': 'the',
        'adn': 'and',
        'thye': 'they',
        'yuo': 'you',
        'i': 'I'
    }
    main(sys.argv[1], sys.argv[2], corrections)