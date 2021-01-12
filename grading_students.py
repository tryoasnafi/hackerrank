# Look at to the case:
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    '''
    res = []
    for grade in grades:
        if grade % 5 > 2 and grade >= 38:
            grade += 5 - (grade % 5)
        res.append(grade)

    return res
    '''
    # One line solution
    return [(e + 5 - (e % 5) if e % 5 > 2 and e >= 38 else e) for e in grades]


if __name__ == '__main__':
    grades_count = int(input())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(*result, sep="\n")
