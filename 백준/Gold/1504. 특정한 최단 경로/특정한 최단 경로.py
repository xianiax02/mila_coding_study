import sys
import heapq
input=sys.stdin.readline
n,e=map(int,input().split())
adlist=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,w=map(int,input().split())
    adlist[a].append((b,w))
    adlist[b].append((a,w))
v1,v2=map(int,input().split())
inf=float('inf')
dist=[[inf]*(n+1) for _ in range(3)]

def search(distnum,start):
    dist[distnum][start]=0
    mq=[] 
    heapq.heappush(mq,(0,start))
    while mq:
        cd,cn=heapq.heappop(mq)
        if cd<=dist[distnum][cn]:
            for nxt,w in adlist[cn]:
                if dist[distnum][nxt]>cd+w:
                    dist[distnum][nxt]=cd+w
                    heapq.heappush(mq,(cd+w,nxt))



for i,start in zip(range(3),[1,n,v1]):
    search(i,start)

answer=min(dist[0][v1]+dist[1][v2],dist[0][v2]+dist[1][v1])+dist[2][v2]
if answer>=inf:
    print(-1)

else:
    print(answer)
