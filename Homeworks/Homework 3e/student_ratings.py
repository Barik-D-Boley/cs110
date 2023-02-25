class Grade:
    def __init__(self, score, comment):
        self.score = score
        self.comment = comment


def main():
    print('Enter ratings for this class.\nEach rating includes a score and a comment.\nUse a blank score to end.')
    student_scores = []

    while True:
        score = input('Score: ')
        if score == '':
            break
        comment = input('Comment: ')
        student_scores.append(Grade(float(score), comment))

    total_score = 0
    average_score = 0

    for i in range(len(student_scores)):
        total_score += student_scores[i].score
        if i+1 == len(student_scores):
            average_score = round(total_score/(i+1), 1)

    print(f'Average rating: {average_score}')
    print('Comments:')

    for i in range(len(student_scores)):
        print(f'- {student_scores[i].comment}')


if __name__ == '__main__':
    main()