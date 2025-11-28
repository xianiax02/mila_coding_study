import sys
from collections import deque
#input=sys.stdin.readline
 #exclude starting point
n,m=map(int,input().strip().split())
graph=[] #0base indexing
visited=[[0]*m for i in range(n)]
visited[0][0]=1
for _ in range(n):
    row=list(map(int,input().strip()))
    graph.append(row)
mq=deque()

mq.append((0,0)) #row,col
dr=[-1,0,1,0]
dc=[0,-1,0,1]

# ⭐추가: 최단거리 누적을 위해 시작점을 1로 초기화


while mq:
    current=mq.popleft()
    if current[0]==n-1 and current[1]==m-1:
        break
    for i,j in zip(dr,dc):
        if -1<current[0]+i<n and -1<current[1]+j<m: #index check
            if not visited[current[0]+i][current[1]+j] and graph[current[0]+i][current[1]+j]==1:
                graph[current[0]+i][current[1]+j]=graph[current[0]][current[1]]+1
                mq.append((current[0]+i,current[1]+j))
                visited[current[0]+i][current[1]+j]=1

print(graph[n-1][m-1])
