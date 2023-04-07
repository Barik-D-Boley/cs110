import sys
import re


class StudentsGrades:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
        
class LetterGrade:
    def __init__(self, grade, students):
        self.grade = grade
        self.students = students


def main(infile, grades_column, students_column):
    students = []
    letter_grades = []

    with open(infile, 'r') as file:
        file_read = file.readlines()

    for i, line in enumerate(file_read):
        modified_line = re.sub('\\n', '', line)
        modified_line = modified_line.split(',')
        students.append(StudentsGrades(modified_line[int(students_column)], modified_line[1:]))

        if modified_line[int(grades_column)] not in [x.grade for x in letter_grades if x.grade == modified_line[int(grades_column)]]:
            letter_grades.append(LetterGrade(modified_line[int(grades_column)], []))

    for letter_grade in letter_grades:
        for student in students:
            if student.grades[int(grades_column)-1] == letter_grade.grade:
                letter_grade.students.append(student.name)
        print(f'{letter_grade.grade}: {letter_grade.students}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])