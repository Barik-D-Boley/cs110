def find_highest_score(scores):
    # Write code here
    pass


def main():
    scores = [('Johns', 'Hayden', 72), ('Rodriguez', 'Emily', 94), ('Young', 'Henry', 91), ('Bean', 'Alma', 95), ('Peterson', 'Roger', 83)]
    last, first, score = find_highest_score(scores)
    print(f"Highest score: {first} {last}, {score}")


if __name__ == '__main__':
    main()
