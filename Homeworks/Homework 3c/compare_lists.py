def main():
    fruit_list = [input('Enter a Fruit: ')]
    while True:
        if fruit_list[len(fruit_list)-1] == '':
            fruit_list.pop()
            break
        else:
            fruit_list.append(input('Enter a Fruit: '))

    vegetable_list = [input('Enter a Vegetable: ')]
    while True:
        if vegetable_list[len(vegetable_list) - 1] == '':
            vegetable_list.pop()
            break
        else:
            vegetable_list.append(input('Enter a Vegetable: '))

    if len(fruit_list) > len(vegetable_list):
        print('Fruits:')
        for i in range(len(fruit_list)):
            print(f' - {fruit_list[i]}')

        print('Vegetables:')
        for i in range(len(vegetable_list)):
            print(f' - {vegetable_list[i]}')
        print('You need more vegetables!')
    elif len(fruit_list) < len(vegetable_list):
        print('Vegetables:')
        for i in range(len(vegetable_list)):
            print(f' - {vegetable_list[i]}')

        print('Fruits:')
        for i in range(len(fruit_list)):
            print(f' - {fruit_list[i]}')
        print('You need more fruit!')
    else:
        print('Fruits:')
        for i in range(len(fruit_list)):
            print(f' - {fruit_list[i]}')

        print('Vegetables:')
        for i in range(len(vegetable_list)):
            print(f' - {vegetable_list[i]}')
        print('What a healthy balanced diet!')


if __name__ == '__main__':
    main()
