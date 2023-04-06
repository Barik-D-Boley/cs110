import sys


def readfile(filename):
    """ Read an entire file and return its contents as one long string. """
    with open(filename) as file:
        return file.read()


def count_words(content, words):
    """
    content -- a string
    words -- a list of strings

    Count how many times each word in <words> appears in <content>.
    Return a dictionary that maps each word in <words> to its count.
    """
    # Write code here
    pass


def print_counts(counts):
    """ Print a dictionary that maps words to counts. """
    for word, count in counts.items():
        print(f"{word}: {count}")

def main(filename):
    # read the file into a long string
    content = readfile(filename)
    # count how often "very" and "really" appear in the string
    counts = count_words(content, ['very', 'really'])
    # print the counts
    print_counts(counts)


if __name__ == '__main__':
    main(sys.argv[1])
