import sys
import re
import random


def main(infile):
    with open(infile, 'r') as file:
        word_list = []
        for line in file:
            word_list.append(re.sub('\\n', '', line))

    random_word = word_list[random.randint(0, len(word_list)-1)]
    # random_word = 'grapefruit'
    # print(random_word)
    # print(re.search(fr'[banana]', random_word))

    while True:
        guess = input('Guess a word: ')

        if guess.lower() == random_word:
            print('That\'s it!')
            break
        elif guess.lower() in random_word:
            print('almost')
        elif bool(re.search(fr'[{guess.lower()}]', random_word)):
            print('close')
        else:
            print('nope')


if __name__ == '__main__':
    main(sys.argv[1])