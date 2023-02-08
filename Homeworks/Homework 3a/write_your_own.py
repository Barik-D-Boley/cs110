def mad_libs():
    print('Welcome to Mad Libs!')
    print('Please enter the following words:')
    adjective = input('Adjective: ')
    noun = input('Noun: ')
    past_tense_verb = input('Past-Tense Verb: ')
    print(f'The {adjective} brown {noun} {past_tense_verb} over the fence')


if __name__ == '__main__':
    mad_libs()