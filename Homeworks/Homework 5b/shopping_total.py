import sys
import re


def main(shopping_cart_infile, items_infile):
    items = {}
    total_cost = 0

    with open(shopping_cart_infile, 'r') as file:
        cart_file = []
        for line in file:
            cart_file.append(re.sub('\\n', '', line).split(','))

    with open(items_infile, 'r') as file:
        items_file = []
        for line in file:
            items_file.append(re.sub('\\n', '', line).split(','))

    for item in items_file:
        items[item[0]] = item[1]

    for item in cart_file:
        total_cost += float(item[1]) * float(items[item[0]])

    print(f'The total is ${round(total_cost, 2)}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])