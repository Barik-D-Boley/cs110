def main():
    words = ['the', 'elephant', 'ate', 'twenty', 'bananas', 'and', 'an', 'orange']
    character_total = 0
    shortest_word = None

    for i in range(len(words)):
        character_total += len(words[i])
        if not shortest_word or len(words[i]) < len(shortest_word):
            shortest_word = words[i]

    print(f'The shortest word is: {shortest_word}')
    print(f'The total length of all the words is: {character_total}')


if __name__ == '__main__':
    main()
