lst=[]
marks=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        marks.append(score)
    s=sorted(set(marks))[1]
    for i,j in sorted(lst):
        if j==s:
            print(i)
    
