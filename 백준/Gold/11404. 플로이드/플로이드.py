import sys
input=sys.stdin.readline
inf=float("inf")
v=int(input().strip())
e=int(input().strip())
graph=[[inf]*(v+1) for _ in range(v+1)] #0-padding
for i in range(1,v+1):
    graph[i][i]=0

for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a][b]=min(graph[a][b],w) #경로 두개 있는 것 고려

for k in range(1,v+1):
    for s in range(1,v+1):
        for e in range(1,v+1):
            graph[s][e]=min(graph[s][k]+graph[k][e],graph[s][e])

for i in range(1,v+1):
    for j in range(1,v+1):
        if graph[i][j]==inf:
            graph[i][j]=0
for i in range(1,v+1):
    print(*graph[i][1:])