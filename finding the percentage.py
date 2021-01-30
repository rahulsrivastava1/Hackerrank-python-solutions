if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if i==query_name:
           data=student_marks[i]
    for j in data:
        sum=sum+j;
    avg=sum/3
    print("{:.2f}".format(avg))
