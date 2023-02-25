class Grade:
    def __init__(self, student, score):
        self.student = student
        self.score = score


def main():
    grades = []

    print('Enter scores for each student.\nEnter a blank student name to end.')

    while True:
        student = input('Student: ')
        if student == '':
            break
        score = int(input('Score: '))
        grades.append(Grade(student, score))

    bonus = float(input('Bonus: '))
    cutoff = int(input('Cutoff: '))

    print('High Scores:')
    for i in range(len(grades)):
        if round(grades[i].score, 1)*(1+bonus) > cutoff:
            print(f'- {round(round(grades[i].score, 1)*(1+bonus), 1)}: {grades[i].student}')


if __name__ == '__main__':
    main()