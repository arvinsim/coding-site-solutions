#!/usr/env/bin python
# https://www.hackerrank.com/challenges/nested-list
# Python 2

n = int(raw_input())
students = []
for x in xrange(n):
    student = []
    for y in xrange(2):
        if y == 0:
            student.append(raw_input())
        elif y == 1:
            # the grades should be of the float datatype
            student.append(float(raw_input()))
    students.append(student)

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# students = [['Prashant', 52.22], ['Kush', 52.223], ['Kant', 52.222], ['Kanti', 52.2222], ['Harshit', 52.22222]]
# students = ['Sona', -25.001], ['Mona', -25.0001], ['Mini', -25.000], ['Rita', -25.0]

# Accumulator function to get the lowest grade among students
f = lambda a, b: a if a[1] < b[1] else b

# Get the students who are POSITION away from the lowest grade
# if we want to get the second lowest, POSITION = 2 to loop twice
# if we wanted to get the third lowest, POSITION = 3 to loop thrice
# and so on
POSITION = 2
for x in xrange(POSITION):
    # Get the student with the lowest grade
    student_with_lowest_grade = reduce(f, students)
    lowest_grade = student_with_lowest_grade[1]
    # Get the students who currently have the lowest grades
    current_lowest_students = [student for student in students if student[1] == lowest_grade]
    # Get the students who don't have the lowest grades
    students = [student for student in students if student[1] != lowest_grade]

current_lowest_students.sort()
for student in current_lowest_students:
    print(student[0])

