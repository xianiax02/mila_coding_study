from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
mq=deque()
adlist=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adlist[a].append(b)
    indegree[b]+=1
answer=[]
for i in range(1,n+1):
    if not indegree[i]:
       mq.append(i)

while mq:
    c=mq.popleft()
    answer.append(c)
    for nxt in adlist[c]:
        indegree[nxt]-=1
        if indegree[nxt]==0:
            mq.append(nxt)
            
if len(answer)!=n:
    print('impossible')
else:
    print(*answer)