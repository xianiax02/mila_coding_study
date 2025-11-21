import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline
print=sys.stdout.write

v,e=map(int,input().strip().split())
graph=[[] for _ in range(v)] #1 base indexing
visited=[False]*(v+1)
for _ in range(e):
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
find=0
def check5BFS(n,level):
    global find
    if find:
        return #이미 찾았으면 깊게 들어가지 않기
    if level>=5:
        find+=1
        return
    for nextnode in graph[n]:
        if not visited[nextnode]:
            visited[nextnode]=True
            check5BFS(nextnode,level+1)
            visited[nextnode]=False  #이 조건이 있어야 한 경로를 완전히 탐색한 후 돌아오면서 그 경로를 없던 걸로 할 수 있음 ( 다시 탐색 가능)

for i in range(0,v):
    if not find:
        visited[i]=True
        check5BFS(i,1)
        visited[i]=False
    else:
        break
print(str(find))