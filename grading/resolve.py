#!/bin/python3

import sys


def solve(grades):
    round_grades = []
    for current_grade in grades:
        if current_grade < 38:
            round_grades.append(current_grade)
            continue
        diff = 5 - current_grade % 5
        round_grade = (current_grade + diff) if diff < 3 else current_grade
        round_grades.append(round_grade)
    return round_grades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
