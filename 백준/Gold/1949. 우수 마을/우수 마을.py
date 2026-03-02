import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
population=[0]+list(map(int,input().split()))
visited=[False]*(1+n)
graph=[[] for _ in range(n+1)]
dp=[[0,0] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def search(x):
    visited[x]=True
    tmp0,tmp1=0,population[x]
    for nxt in graph[x]:
        if not visited[nxt]: #방문하지 않은 이웃==자식들
            child=search(nxt)
            tmp0+=max(child)
            tmp1+=child[0]
    dp[x]=[tmp0,tmp1]
    return [tmp0,tmp1]
            
search(1)
print(max(dp[1]))            