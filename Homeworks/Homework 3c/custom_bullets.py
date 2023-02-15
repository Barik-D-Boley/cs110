def main():
    item_list = [input('Item: ')]
    while True:
        if item_list[len(item_list)-1] == '':
            item_list.pop()
            print('')
            break
        else:
            item_list.append(input('Item: '))

    bullet_list = [input('Custom Bullet Point: ')]
    while True:
        if bullet_list[len(bullet_list)-1] == '':
            bullet_list.pop()
            print('')
            break
        else:
            bullet_list.append(input('Custom Bullet Point: '))

    for i in range(len(bullet_list)):
        for j in range(len(item_list)):
            print(f'{bullet_list[i]} {item_list[j]}')
        print('')


if __name__ == '__main__':
    main()