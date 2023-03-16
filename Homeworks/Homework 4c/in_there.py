import sys


def main(secret):
    while True:
        guess = input('Guess: ')
        if guess == secret:
            print('You got it!')
            break
        elif secret in guess:
            print('It\'s in there...')
        else:
            print('Nope.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("This program takes one argument, a superlative.")
        print("For example: 'stupendous' or 'fantastic'")
        exit()

    superlative = sys.argv[1]
    main(superlative)