from collections import deque
import sys
input=sys.stdin.readline
n=int(input().strip())
q=deque()
for num in range(1,n+1):
    q.append(num)

while q[0]!=q[-1]:
    q.popleft()
    q.append(q.popleft())

sys.stdout.write(str(q[-1]))
    