def out_of_stock():
    blocked_items = []
    shopping_list = []

    print('What items are out of stock?')
    while True:
        blocked_item = input('Item: ')
        if blocked_item == '':
            break
        blocked_items.append(blocked_item)

    print('What items would you like to purchase?')
    while True:
        buy_item = input('Item: ')
        if any(x in buy_item for x in blocked_items):
            print(f'I\'m sorry, the item {buy_item.upper()} is out of stock.')
        elif buy_item == '':
            break
        else:
            shopping_list.append(buy_item)

    print(f'You have {len(shopping_list)} items:')
    for i in range(len(shopping_list)):
        print(f'- {shopping_list[i]}')

if __name__ == '__main__':
    out_of_stock()