def main():
    print('Let\'s concatenate strings!')
    while 1:
        string1 = input('Enter a string: ')
        string2 = input('Enter a string: ')
        if string1 < string2:
            print(f'The result is: {string1+string2}')
        elif string1 > string2:
            print(f'Sorry, {string1} is less than {string2}. I\'m quitting.')
            break


if __name__ == '__main__':
    main()



