import sys
import heapq
input=sys.stdin.readline
n,m,x=map(int,input().split())
adlist=[[] for _ in range(n+1)]
radlist=[[] for _ in range(n+1)]
inf=float('inf')
distance1=[0]+[inf]*n #going to party
distance2=[0]+[inf]*n #going back home
for _ in range(m):
    a,b,w=map(int,input().split())
    adlist[a].append((b,w))
    radlist[b].append((a,w))

#filling going to party
mq=[]
heapq.heappush(mq,(0,x))
distance1[x]=0
while mq:
    cd,cn=heapq.heappop(mq)
    if cd<=distance1[cn]:
        for nxt,w in radlist[cn]:
            if distance1[nxt]>cd+w:
                distance1[nxt]=cd+w
                heapq.heappush(mq,(cd+w,nxt))

#filling going back home
mq=[]
heapq.heappush(mq,(0,x))
distance2[x]=0
while mq:
    cd,cn=heapq.heappop(mq)
    if cd<=distance2[cn]:
        for nxt,w in adlist[cn]:
            if distance2[nxt]>cd+w:
                distance2[nxt]=cd+w
                heapq.heappush(mq,(cd+w,nxt))

totaldistance=[i+j for i,j in zip(distance1,distance2)]
print(max(totaldistance))

