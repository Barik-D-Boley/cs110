def main():
    verb_list = []

    while True:
        verb = input('Enter a verb ending in "ing": ')
        if verb == '':
            break
        else:
            verb_list.append(verb)

    for i in range(len(verb_list)):
        print(f'The puppy is {verb_list[i]}!')
    print('The puppy is taking a nap.')


if __name__ == '__main__':
    main()
