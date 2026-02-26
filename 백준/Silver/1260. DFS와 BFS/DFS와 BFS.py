import sys
from collections import deque
input=sys.stdin.readline
mq=deque()
n,m,v=map(int,input().split())
adlist=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    adlist[a].append(b)
    adlist[b].append(a)
for i in range(n+1):
    adlist[i].sort()
bfs=[v]
dfs=[]
mq.append(v)
visited[v]=True
while mq:
    c=mq.popleft()
    for nxt in adlist[c]:
        if not visited[nxt]:
            mq.append(nxt)
            visited[nxt]=True
            bfs.append(nxt)
visited=[False]*(n+1)
visited[v]=True
def dfsf(v):
    dfs.append(v)
    for nxt in adlist[v]:
        if not visited[nxt]:
            visited[nxt]=True
            dfsf(nxt)
dfsf(v)
print(*dfs)
print(*bfs)