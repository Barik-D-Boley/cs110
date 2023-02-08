def main():
    while 1:
        print('What would you like to do?\n1) Receive compliment\n2) Receive advice\n3) Quit')
        choice = input('Option: ')
        if int(choice) == 1:
            print('\nYou have nice hair!\n')
        elif int(choice) == 2:
            print('\nEating food gives you energy\n')
        elif int(choice) == 3:
            print('\nGoodbye!')
            break
        else:
            print('\nThat was not one of the options. Try again.\n')


if __name__ == '__main__':
    main()