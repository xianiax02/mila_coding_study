import sys
import heapq
input=sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
adlist=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,w=map(int,input().split())
    adlist[a].append((b,w))
mq=[]
inf=float('inf')
distance=[inf]*(v+1)
distance[start]=0
heapq.heappush(mq,(0,start))
while mq:
    cd,cn=heapq.heappop(mq)
    if cd<=distance[cn]:
        distance[cn]=cd
        for nxt,nw in adlist[cn]:
            if cd+nw<distance[nxt]:
                distance[nxt]=cd+nw
                heapq.heappush(mq,(cd+nw,nxt))
for i in range(1,len(distance)):
    dist=distance[i]
    if dist==inf:
        print('INF')
    else:
        print(dist)
