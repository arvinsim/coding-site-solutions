#!/usr/env/bin python

# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage

number_of_students = raw_input()
students = {}
for i in xrange(int(number_of_students)):
    student_input = raw_input()
    student = student_input.split(' ')
    students[student[0]] = [student[1], student[2], student[3]]
student_average_to_print = raw_input()

# students = {'krishna': ['67', '68', '69'], 'malika': ['52', '56', '60'], 'arjun': ['70', '98', '63']}
# student_average_to_print = 'malika'

f = lambda x, y: float(x) + float(y)
student_total = reduce(f, students[student_average_to_print])
student_number_of_grades = len(students[student_average_to_print])
student_average = student_total/student_number_of_grades
print("{:.2f}".format(student_average))
