def play(secret_word):
    secret_word = 'python'
    guess = input('Guess a word: ')

    while True:
        if guess == secret_word:
            print('You got it!')
            break
        elif guess > secret_word:
            print('Lower!')
            guess = input('Guess a word: ')
        elif guess < secret_word:
            print('Higher!')
            guess = input('Guess a word: ')


if __name__ == '__main__':
    play('python')