def mad_libs_short():
    print('Welcome to Mad Libs!\nPlease enter the following words:')
    noun1 = input('Noun: ')
    adjective = input('Adjective: ')
    noun2 = input('Noun: ')
    character = input('Character: ')
    animal = input('Animal (Plural): ')
    print(f'{noun1} sat on a {noun2}. {noun1} had a {adjective} fall. All {character}\'s {animal} and all the {character}\'s men couldn\'t put {noun1} together again.')


if __name__ == '__main__':
    mad_libs_short()

