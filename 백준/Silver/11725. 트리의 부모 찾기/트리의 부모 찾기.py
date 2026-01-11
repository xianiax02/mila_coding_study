from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
mq=deque()
parent=[0]*(n+1)
tree=[[] for _ in range(1+n)] #0-padding
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

mq.append(1)
parent[1]=1
while mq:
    currentnode=mq.popleft()
    for nextnode in tree[currentnode]:
        if not parent[nextnode]:
            mq.append(nextnode)
            parent[nextnode]=currentnode

for i in range(2,n+1):
    print(parent[i])