import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
n,l=map(int,input().split())
numbers=list(map(int,input().split()))
mq=deque()
for i,num in enumerate(numbers):
    if mq and mq[0][1]<i-l+1:
        mq.popleft()
    while mq and mq[-1][0]>num:
        mq.pop()
    mq.append((num,i))
    print(str(mq[0][0])+' ')
    