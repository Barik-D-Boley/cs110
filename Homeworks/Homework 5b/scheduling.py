import sys
import re


def main(names_infile, time_infile):
    student_schedule = {}

    with open(names_infile, 'r') as file:
        names_file = []
        for line in file:
            names_file.append(re.sub('\\n', '', line))

    with open(time_infile, 'r') as file:
        times_file = []
        for line in file:
            times_file.append(re.sub('\\n', '', line))

    for i, x in enumerate(names_file):
        student_schedule[names_file[i]] = times_file[i]

    while True:
        name = input('Name: ')
        if name == '':
            break
        print(f'{name} is {f"assigned {student_schedule[name]}" if name in student_schedule.keys() else "not assigned a timeslot"}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])