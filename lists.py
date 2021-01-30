N=int(input())
lst=[]
for i in range(N):
    args=input().split(" ")
    if args[0]=="print":
        print(lst)
    if args[0]=="append":
        lst.append(int(args[1]))
    if args[0]=="insert":
        lst.insert(int(args[1]),int(args[2]))
    if args[0]=="pop":
        lst.pop()
    if args[0]=="sort":
        lst.sort()
    if args[0]=="remove":
        lst.remove(int(args[1]))
    if args[0]=="reverse":
        lst.reverse()
