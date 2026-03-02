import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
inf=float('inf')
distance=[[inf]*(1+n) for _ in range(n+1)]
for i in range(1,n+1):
    distance[i][i]=0
for _ in range(m):
    a,b,w=map(int,input().split())
    distance[a][b]=min(distance[a][b],w) #주의

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==inf:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()