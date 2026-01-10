import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
v,e=map(int,input().split())
graph=[]
for _ in range(e):
    a,b,w=tuple(map(int,input().split()))
    graph.append((w,a,b))
rootgraph=[i for i in range(v+1)] #0-padding 까먹음
graph.sort()
result=[]
def find(x):
    if rootgraph[x]==x:
        return x
    rootgraph[x]=find(rootgraph[x])
    return rootgraph[x]

def union(a,b):
    roota=find(a)
    rootb=find(b)
    rootgraph[max(roota,rootb)]=min(roota,rootb)

for edge in graph:
    w,a,b=edge
    roota=find(a)
    rootb=find(b)
    if roota==rootb:
        continue
    else:
        union(a,b)
        result.append(edge)

ans=0
for edge in result:
    ans+=edge[0]

print(ans)