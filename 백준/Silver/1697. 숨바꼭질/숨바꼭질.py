import sys
from collections import deque
n,k=map(int,sys.stdin.readline().strip().split(' '))
visited=[False]*100001
queue=deque()
queue.append((n,0))
while queue:
    a,level=queue.popleft()
    if a==k:
        sys.stdout.write(str(level))
        break
    for nextpos in (a-1,a+1,a*2):
        if 0<=nextpos<100001:
            if not visited[nextpos]:
                queue.append((nextpos,level+1))
                visited[nextpos]=True