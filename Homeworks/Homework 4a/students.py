class Student:
    def __init__(self, name, hometown, school):
        self.name = name
        self.hometown = hometown
        self.school = school

def main():
    students = []

    while True:
        print('Enter a student.')
        name = input('Name: ')
        if name == '':
            break
        hometown = input('Hometown: ')
        school = input('School: ')
        students.append(Student(name, hometown, school))

    print('BYU Students:')
    for i in range(len(students)):
        if students[i].school.lower() == 'byu':
            print(f'- {students[i].name.upper()}')

    print('Other Students:')
    for i in range(len(students)):
        if not students[i].school.lower() == 'byu':
            print(f'- {students[i].name}')

if __name__ == '__main__':
    main()