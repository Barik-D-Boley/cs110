def reverse_wordle():
    blocked_characters = list(set([*input('Characters to block: ')]))
    replacement = input('Replacement: ')

    while True:
        word = [*input('Word: ')]
        if not len(word):
            break
        else:
            for i in range(len(word)):
                for j in range(len(blocked_characters)):
                    if word[i].lower() == blocked_characters[j].lower():
                        word[i] = replacement
            print(''.join(str(i) for i in word))


if __name__ == '__main__':
    reverse_wordle()