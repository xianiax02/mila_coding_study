import sys
sys.setrecursionlimit(10**6)
import heapq
input=sys.stdin.readline
v,e=map(int,input().split())
edgelist=[]
parent=[i for i in range(v+1)]
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[max(a,b)]=min(a,b)

for _ in range(e):
    a,b,w=map(int,input().split())
    edgelist.append((w,a,b))
edgelist.sort()
answer=0
cnt=0
for w,a,b in edgelist:
    a,b=find(a),find(b)
    if a!=b:
        union(a,b)
        answer+=w
        cnt+=1
        if cnt==v-1:
            break
    
    
print(answer)
    