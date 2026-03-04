import sys
input=sys.stdin.readline
v,e=map(int,input().split())
inf=float('inf')
graph=[[inf]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a][b]=w

for k in range(1,v+1):
    for i in range(1,v+1):
        if graph[i][k]==inf:
            continue
        for j in range(1,v+1):
            graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])

answer=min([graph[i][i] for i in range(1,v+1)])
if answer==inf:
    print(-1)
else:
    print(answer)