import sys


def main(topic):
    votes = {}

    while True:
        vote = input(f'{topic}: ')
        if vote == '':
            break
        if not vote in votes.keys():
            votes[vote] = 1
        else:
            votes[vote] += 1

    print(votes)


if __name__ == '__main__':
    main(sys.argv[1])