def mad_libs():
    print('Welcome to Mad Libs!\nPlease enter the following words:')
    noun1 = input('Noun: ')
    adjective1 = input('Adjective: ')
    adjective2 = input('Adjective: ')
    noun2 = input('Noun: ')
    number = input('Number: ')
    adjective3 = input('Adjective: ')
    past_tense_verb = input('Past-Tense Verb: ')
    game = input('Game: ')
    verb = input('Verb: ')
    print(f'Once upon a time a student at found themselves in a {noun1} class. The teacher was so {adjective1} that the student started to daydream about a {noun2}. Then the student woke up and realized that they were still in class. The teacher was so {adjective2} that they gave the student a {number} on the assignment. The student was so {adjective3} that he {past_tense_verb} the class and went home to play {game}. The moral of the story is that you should never {verb} in class.')


if __name__ == '__main__':
    mad_libs()