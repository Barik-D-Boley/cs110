def main():
    word_list = [input('Word: ')]
    small_list = []
    big_list = []

    # Asks for words until no word is presented
    while True:
        if word_list[len(word_list)-1] == '':
            break
        else:
            word_list.append(input('Word: '))

    boundary = input('Boundary: ')
    print(f'You have {len(word_list) - 1} words')

    # Sorts words into nig or small list
    for i in range(len(word_list) - 1):
        if word_list[i] < boundary:
            small_list.append(word_list[i])
        elif word_list[i] > boundary:
            big_list.append(word_list[i])

    # Prints the big and small lists
    print('These are small:')
    for i in range(len(small_list)):
        print(small_list[i])
    print('These are big:')
    for i in range(len(big_list)):
        print(big_list[i])



if __name__ == '__main__':
    main()