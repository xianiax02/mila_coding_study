import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    lst=[]
    cnt=0
    for _ in range(n):
        lst.append(tuple(map(int,input().split())))
    lst.sort()
    maxs1,mins2=0,float('inf')
    for i in range(len(lst)):
        if lst[i][0]>maxs1 and lst[i][1]>mins2:
           cnt+=1
        else:
            maxs1=max(lst[i][0],maxs1)
            mins2=min(lst[i][1],mins2)
    print(len(lst)-cnt)