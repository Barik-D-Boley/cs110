def main():
    while 1:
        print('I can add numbers for you!')
        number1 = input('Enter a number: ')
        number2 = input('Enter a number: ')
        print(f'Your result is: {int(number1)+int(number2)}')
        go_again = input('Would you like to do more? ').lower()
        if go_again == 'no' or go_again == 'n' or go_again == 'false':
            break


if __name__ == '__main__':
    main()