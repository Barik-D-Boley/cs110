def add_numbers(list1, list2):
    """
    Takes two lists of numbers.
    Returns a new list that adds each corresponding item together from
    list1 and list 2.
    """
    # Write code here
    pass



def enter_list():
    numbers = []
    print("Enter a list of numbers!")
    while True:
        number = input("Number: ")
        if number == '':
            break
        numbers.append(int(number))

    return numbers


def main():
    list1 = enter_list()
    list2 = enter_list()
    results = add_numbers(list1, list2)
    print(results)


if __name__ == '__main__':
    main()
