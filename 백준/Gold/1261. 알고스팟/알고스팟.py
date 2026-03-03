import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))
brokenwalls=[[-1]*m for _ in range(n)]
di=[-1,0,1,0]
dj=[0,-1,0,1]
mq=deque()
#0,0 에서 n-1,m-1로 가야함.
mq.append((0,0)) #i,j,cost
brokenwalls[0][0]=0
while mq:
    ci,cj=mq.popleft()
    for ddi,ddj in zip(di,dj):
        ni,nj=ci+ddi,cj+ddj
        if -1<ni<n and -1<nj<m and brokenwalls[ni][nj]==-1: #방문 안했던 지점을 방문/ 벽을 안뚫을 수 있는 경로를 0-1 bfs를 통해 먼저 방문하므로 mi 필요 x
            brokenwalls[ni][nj]=brokenwalls[ci][cj]+graph[ni][nj]
            if graph[ni][nj]:
                mq.append((ni,nj))
            else:
                mq.appendleft((ni,nj))
            
print(brokenwalls[n-1][m-1])
