import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
counts=[0]*10001
for _ in range(n):
    counts[int(input().strip())]+=1

for i in range(10001):
    if counts[i]:
        for _ in range(counts[i]):
            print(str(i)+'\n')