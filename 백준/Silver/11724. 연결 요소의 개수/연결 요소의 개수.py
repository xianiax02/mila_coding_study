import sys
sys.setrecursionlimit(10000)
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().strip().split())
graph=[[] for _ in range(n+1)] #어차피 0노드는 아무것도 안넣으면 되니 단순 n+1로 처리함. 
visited=[1]+[0]*n #노드가 0부터가 아니라 1부터 시작하므로 인덱싱에 주의해서 1 based index로 설정함. 초기에 0으로 설정하면 unvisited로 간주해서 카운트하기 때문에 조심. 
ms=deque()
for _ in range(m):
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
def DFS(start):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
cnt=0
for node in range(1,n+1):
    if not visited[node]:
        DFS(node)
        cnt+=1

print(cnt)


#쉬운 구현법



