def do_counts():
    # initialize counts
    counts = {}
    while True:
        word = input("Word: ")
        if word == '':
            break
        # Write code here
        # You need to:
        # (1) check if word is in the counts dictionary
        # (2) if it is not, initialize the count for that word to zero
        # (3) increment the count for that word by one


    return counts


def main():
    counts = do_counts()
    print(counts)


if __name__ == '__main__':
    main()