import sys
import heapq
input=sys.stdin.readline
n=int(input())
mq=[]
for _ in range(n):
    heapq.heappush(mq,int(input()))
ans=0
while len(mq)>1:
    a=heapq.heappop(mq)
    b=heapq.heappop(mq)
    ans+=a+b
    heapq.heappush(mq,a+b)

print(ans)