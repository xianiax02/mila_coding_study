import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

DP=[[0]*(1+m) for _ in range(1+n)]
for row in range(1,n+1):
    for col in range(1,m+1):
        if graph[row-1][col-1]: #0-base 1-base 혼용시 주의 각각 분리해서 생각
            DP[row][col]=min(DP[row-1][col-1],DP[row-1][col],DP[row][col-1])+1
        else:
            DP[row][col]=0 #자기를 포함할 수 없으므로

maxnum=0
for row in range(1,n+1):
    maxnum=max(max(DP[row]),maxnum)

print(maxnum**2)