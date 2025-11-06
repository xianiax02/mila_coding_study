from collections import deque
import sys

input=sys.stdin.readline
n=int(input().strip())
numbers=list(map(int,input().strip().split()))
d=deque()
answer=[0]*n

for index in range(n):   
    while d and numbers[d[-1]]<numbers[index]:
        answer[d.pop()]=numbers[index]
    d.append(index)

while d:
    answer[d.pop()]=-1

a=' '.join(map(str,answer))
sys.stdout.write(str(a))

    
