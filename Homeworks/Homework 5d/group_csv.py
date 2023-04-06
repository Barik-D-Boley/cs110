import sys
import re


class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades


def main(infile, grades_column, students_column):
    students = []
    grades = []

    with open(infile, 'r') as file:
        file_read = file.readlines()

    print(file_read)

    for i, line in enumerate(file_read):
        modified_line = re.sub('\\n', '', line)
        modified_line = modified_line.split(',')
        students.append(Student(modified_line[0], modified_line[1:]))
        print(students[i].name, students[i].grades)




if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])