import random
import sys
import re


def main(infile, max_guesses):
    with open(infile, 'r') as file:
        word_bank = file.readlines()
        answer = word_bank[random.randint(0, len(word_bank)-1)]

    guess_number = 0

    while guess_number < int(max_guesses):
        guess = input(f'Guess # {guess_number+1}: \n').lower()

        # if not re.match('^[a-zA-Z]{5}$', guess):
        #     print(f'\nGuesses must be 5 characters long and can only include alphabetical characters\nTry again\n')
        #     continue

        wordle_output = []
        for i, letter in enumerate(guess):
            if letter == answer[i]:
                wordle_output.append('!')
            elif letter in answer:
                wordle_output.append('?')
            else:
                wordle_output.append('*')

        print(''.join(wordle_output))
        if ''.join(wordle_output) == '!!!!!':
            print('Way to go!')
            break
        guess_number += 1

    if guess_number == int(max_guesses):
        print(f'Maybe next time. The answer is {answer.strip()}.')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])