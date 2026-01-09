import sys
input=sys.stdin.readline
v,e=map(int,input().split())
graph=[[] for _ in range(e)] 
inf=float('inf')
distance=[inf]*(v+1) #0-padding
distance[1]=0
for i in range(e):
    a,b,w=map(int,input().split())
    graph[i]=[a,b,w]

for _ in range(v-1):
    for start,end,time in graph:
        if distance[start]!=inf and distance[end]>distance[start]+time:
            distance[end]=distance[start]+time

mcycle=False
for start,end,time in graph:
    if distance[start]!=inf and distance[end]>distance[start]+time:
        mcycle=True
        
if mcycle:
    print(-1)
else:
    for time in distance[2:]: #출력형식 오류 2번도시부터 출력해야함.
        if time==inf:
            print(-1)
        else:
            print(time)