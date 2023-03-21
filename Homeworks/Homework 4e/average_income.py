import sys


def main(infile, profession):
    profession_customers = []
    total_income = 0

    with open(infile, 'r') as file:
        for line in file:
            if line.split(',')[5] == profession:
                profession_customers.append(line)
                total_income += int(line.split(',')[3])

    print(f'The average income of {profession} is {round(total_income/len(profession_customers))}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])