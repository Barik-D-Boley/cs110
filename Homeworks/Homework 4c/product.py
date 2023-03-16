import sys


def main(numbers):
    del numbers[0]
    total_product = 1
    for i in range(len(numbers)):
        total_product *= float(numbers[i])
    print(total_product)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("This program takes one argument, a superlative.")
        print("For example: 'stupendous' or 'fantastic'")
        exit()

    superlative = sys.argv
    main(superlative)