

def print_info(ratings, flavor):
    average = get_average(ratings)
    print(f"The average rating for {flavor} is {average}.")


def get_ratings():
    # Write code here
    pass


def get_flavors():
    # Write code here
    pass


def main():
    ratings = get_ratings()
    flavors = get_flavors()
    for flavor in flavors:
        new_ratings = ratings_for_flavor(ratings, flavor)
        print_info(new_ratings, flavor)


if __name__ == '__main__':
    main()
