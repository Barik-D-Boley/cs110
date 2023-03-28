import sys


def main(infile, outfile, age):
    old_customers = []

    with open(infile, 'r') as file:
        for line in file:
            if line.split(',')[2] == 'Age' or int(line.split(',')[2]) > int(age):
                old_customers.append(line)

    with open(outfile, 'w') as file:
        file.writelines(old_customers)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])