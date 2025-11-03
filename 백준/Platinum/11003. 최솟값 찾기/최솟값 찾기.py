import sys
from collections import deque
input=sys.stdin.readline
n,l=map(int,input().strip().split())
numbers=list(map(int,input().strip().split()))
mydeque=deque()
for i in range(n):
    while mydeque and mydeque[-1][1]>numbers[i]:
        mydeque.pop()
    mydeque.append((i,numbers[i]))
    if mydeque[0][0]<=i-l:
        mydeque.popleft()
    sys.stdout.write(str(mydeque[0][1])+' ')
                  
        