

def print_info(ratings, flavor):
    average = get_average(ratings)
    print(f"The average rating for {flavor} is {average}.")


def get_ratings():
    ratings = []
    print('Enter all the ice cream ratings. Enter an empty flavor to end.')
    while True:
        flavor = input('Enter a flavor: ')
        if flavor == '':
            break
        rating = float(input('Enter a rating: '))
        ratings.append((flavor, rating))
    return ratings


def get_flavors():
    flavors = []
    print('Enter flavors to get info on, ending with a blank line.')
    while True:
        flavor = input('Flavor: ')
        if flavor == '':
            break
        flavors.append(flavor)
    return flavors


def main():
    ratings = get_ratings()
    flavors = get_flavors()

    for flavor in flavors:
        flavor_ratings = []
        for i in range(len(ratings)):
            if flavor == ratings[i][0]:
                flavor_ratings.append(ratings[i])

        total_ratings = 0
        for i in range(len(flavor_ratings)):
            total_ratings += flavor_ratings[i][1]

        print(f'The average rating for {flavor} is {round(total_ratings / len(flavor_ratings), 1)}')


if __name__ == '__main__':
    main()
