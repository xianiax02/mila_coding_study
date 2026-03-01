import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
dp=[[-1]*2 for _ in range(1+n)]
graph=[[] for _ in range(1+n)]
population=[0]+list(map(int,input().split()))
visited=[False]*(1+n)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b) #큰 번호가 자식이 되도록 단방향으로 설정
    graph[b].append(a)

def filldp(x):
    visited[x]=True
    a,b=0,population[x] #0,1 값
    for c in graph[x]:
        if not visited[c]:
            tmp=filldp(c)
            a+=max(tmp[1],tmp[0])
            b+=tmp[0] #자식은 우수마을이 아니어야함.
    dp[x]=[a,b]
    return [a,b]

filldp(1)
print(max(dp[1]))