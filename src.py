if __name__ == '__main__':
    def calculate_avg(list_of_grades):
        number_of_grades = len(list_of_grades)
        sum_of_grades = sum(list_of_grades)

        return "%.2f" % (sum_of_grades / number_of_grades)


    n = int(input())
    assert 2 <= n <= 10
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        for sc in range(0, len(scores)):
            assert type(scores[sc]) == int or float
            assert 0 <= scores[sc] <= 100
        student_marks[name] = scores

    query_name = input()
    assert query_name in student_marks.keys()
    print(calculate_avg(student_marks.get(query_name)))
