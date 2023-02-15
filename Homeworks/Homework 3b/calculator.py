def calculator():
    print('\nWhat would you like to do?\n 1) Add\n 2) Subtract\n 3) Quit')
    option = input('Option: ')

    while True:
        if option == '1':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{int(number1)+int(number2)}')
            print('\nWhat would you like to do?\n 1) Add\n 2) Subtract\n 3) Quit')
            option = input('Option: ')
        elif option == '2':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{int(number1)-int(number2)}')
            print('\nWhat would you like to do?\n 1) Add\n 2) Subtract\n 3) Quit')
            option = input('Option: ')
        elif option == '3':
            break
        else:
            print(f'Unrecognized response: {option}')
            print('\nWhat would you like to do?\n 1) Add\n 2) Subtract\n 3) Quit')
            option = input('Option: ')


if __name__ == '__main__':
    calculator()
