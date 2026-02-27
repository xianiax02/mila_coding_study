import heapq
import sys
input=sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
inf=float('inf')
dist=[inf]*(v+1)
adlist=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,w=map(int,input().split())
    adlist[a].append((b,w))
dist[start]=0
mq=[(0,start)]
while mq:
    d,node=heapq.heappop(mq)
    if d<=dist[node]:
        for nxtnode,nxtdist in adlist[node]:
            if dist[node]+nxtdist<dist[nxtnode]:
                dist[nxtnode]=dist[node]+nxtdist
                heapq.heappush(mq,(dist[node]+nxtdist,nxtnode))

for d in dist[1:]:
    if d==inf:
        print('INF')
    else:
        print(d)
            
    
    