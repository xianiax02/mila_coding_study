import sys
from bisect import bisect_left
input=sys.stdin.readline
n=int(input())
numbers=list(map(int,input().split()))
d=[]
for num in numbers:
    idx=bisect_left(d,num)
    if idx==len(d): #끝에 올때
        d.append(num)
    else:
        d[idx]=num
print(len(d))