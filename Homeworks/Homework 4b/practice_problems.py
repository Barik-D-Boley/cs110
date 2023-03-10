import re


def doubles(text):
    new_sentence = [*text]

    for i in range(len(new_sentence)-1):
        if new_sentence[i] == 'e' and new_sentence[i+1] == 'e':
            new_sentence[i] = 'eeeee'
            i += 1
        elif (new_sentence[i] == 'o' and new_sentence[i+1] == 'o'):
            new_sentence[i] = 'ooooo'
            i += 1

    return ''.join(str(i) for i in new_sentence)


def for_reals(text):
    new_sentence = [*text]

    for i in range(len(new_sentence)):
        if new_sentence[i] == '%':
            new_sentence[i] = ' percent'
        elif new_sentence[i] == '!':
            new_sentence[i] = ' (for reals).'

    return ''.join(str(i) for i in new_sentence)


def only_o(text):
    vowel_filter = re.compile('[aeiouAEIOU]')
    new_sentence = [*text]

    for i in range(len(new_sentence)):
        if vowel_filter.match(new_sentence[i]) and new_sentence[i].isupper():
            new_sentence[i] = 'O'
        elif vowel_filter.match(new_sentence[i]) and not new_sentence[i].isupper():
            new_sentence[i] = 'o'

    return ''.join(str(i) for i in new_sentence)


def upper_vowels(text):
    vowel_filter = re.compile('[aeiouAEIOU]')
    new_sentence = [*text]

    for i in range(len(new_sentence)):
        if vowel_filter.match(new_sentence[i]):
            new_sentence[i] = new_sentence[i].upper()

    return ''.join(str(i) for i in new_sentence)