import sys


def main(infile):
    with open(infile, 'r') as file:
        file_text = file.read()
        number_list = ' '.join(file_text.split('\n')).split(' ')
        number_sum = 0

        for number in number_list:
            if number != '':
                number_sum += int(number)

        print(f'The total is {number_sum}')


if __name__ == '__main__':
    main(sys.argv[1])