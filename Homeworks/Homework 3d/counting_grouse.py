def main():
    grouse_by_area = []
    smallest_grouse_count = None
    largest_grouse_count = None

    while True:
        grouse_count = input('Enter an observation count: ')
        if grouse_count == '':
            break
        else:
            grouse_count = int(grouse_count)

            grouse_by_area.append(grouse_count)
            if not smallest_grouse_count or grouse_count < smallest_grouse_count:
                smallest_grouse_count = grouse_count
            if not largest_grouse_count or grouse_count > largest_grouse_count:
                largest_grouse_count = grouse_count

    print(f'There are {sum(grouse_by_area)} total grouse.')
    print(f'The smallest count is: {smallest_grouse_count}\nThe largest count is: {largest_grouse_count}')

    factor = int(input('Enter factor: '))

    print('The estimated grouse populations are:')
    for i in range(len(grouse_by_area)):
        print(f'- {grouse_by_area[i]*factor}')


if __name__ == '__main__':
    main()
