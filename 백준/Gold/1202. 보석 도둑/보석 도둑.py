import sys
import heapq
input=sys.stdin.readline
n,k=map(int,input().split())
gems=[]
bags=[]
gemlist=[]
answer=0
for _ in range(n):
    gems.append(tuple(map(int,input().split())))
for _ in range(k):
    bags.append(int(input()))
bags.sort()
gems.sort()
pos=0
for bag in bags:
    while pos<n and gems[pos][0]<=bag:
        m,v=gems[pos]
        heapq.heappush(gemlist,(-v,m))
        pos+=1
    if gemlist:
        sv,sm=heapq.heappop(gemlist)
        answer-=sv
print(answer)