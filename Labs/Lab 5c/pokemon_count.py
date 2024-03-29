import sys


def readlines(filename):
    """ Read a file and return a list of lines. """
    with open(filename) as file:
        return file.readlines()


def count_pokemon(lines):
    """
    lines: a list of lines, each line is a comma-separated list of values

    Count all of the Pokemon of each type. The type is in column 4
    of the CSV.

    Return a dictionary that maps type to its count.
    """
    # Write code here
    pass


def print_counts(counts):
    """ Print a dictionary that maps words to counts. """
    for value, count in counts.items():
        print(f"{value}: {count}")


def main(filename):
    # read all the lines of the file
    lines = readlines(filename)
    # count the Pokemon of each type
    counts = count_pokemon(lines)
    print_counts(counts)


if __name__ == '__main__':
    main(sys.argv[1])
