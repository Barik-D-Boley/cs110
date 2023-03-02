def main():
    scores = [('Johns', 'Hayden', 72), ('Rodriguez', 'Emily', 94), ('Young', 'Henry', 91), ('Bean', 'Alma', 95), ('Peterson', 'Roger', 83)]
    high_score = None
    for i in range(len(scores)):
        if not high_score or scores[i][2] > high_score[2]:
            high_score = scores[i]
    print(f"Highest score: {high_score[0]} {high_score[1]}, {high_score[2]}")


if __name__ == '__main__':
    main()
