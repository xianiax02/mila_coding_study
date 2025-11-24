import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
ms=deque()
n,m=map(int,input().strip().split())
visited=[False]*(n+1) #1 base indexing
def DFS(m,n,depth):
    global ms
    if depth==m+1:
        print(' '.join(map(str,ms))+'\n')
        return
    for i in range(1,n+1):
        if not visited[i]:
            ms.append(i)
            visited[i]=True
            DFS(m,n,depth+1)
            ms.pop()
            visited[i]=False

DFS(m,n,1)
