from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(1+n)
adlist=[[] for _ in range(1+n)]
for _ in range(m):
    a,b=map(int,input().split())
    adlist[a].append(b)
    indegree[b]+=1

mq=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        mq.append(i)
answer=[]
while mq:
    c=mq.popleft()
    answer.append(c)
    for nxt in adlist[c]:
        indegree[nxt]-=1
        if indegree[nxt]==0:
            mq.append(nxt)

print(*answer)