import sys
input=sys.stdin.readline
n,m=map(int,input().split())
taller=[0]*(n+1)
smaller=[0]*(n+1)
graph=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a]|=(1<<b)

for k in range(1,n+1):
    for i in range(1,n+1):
        if graph[i]&(1<<k): #i가 k 보다 작다면, i는 k보다 큰 애들에 대해 다 작다.
            graph[i]|=graph[k]

answer=0
for i in range(1,n+1):
    taller=bin(graph[i]).count('1')
    smaller=0
    for row in range(1,n+1):
        if (graph[row]>>i)&1:
            smaller+=1
    if smaller+taller==n-1:
        answer+=1
        
print(answer)