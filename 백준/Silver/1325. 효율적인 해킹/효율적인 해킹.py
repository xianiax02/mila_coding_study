import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)] #0 padding
mq=deque()
answerlist=[1]*(n+1) #각노드에서 연결 될 수 있는 노드 기록하는 곳
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
    
for targetnode in range(1,n+1):
    visited=[False]*(n+1)
    mq.append(targetnode)
    visited[targetnode]=True #잊지말기
    while mq:
        currentnode=mq.popleft()
        for nextnode in graph[currentnode]:
            if not visited[nextnode]:
                mq.append(nextnode)
                visited[nextnode]=True #이거 까먹음..
                answerlist[targetnode]+=1
                
maxnum=max(answerlist)
for i,j in enumerate(answerlist):
    if j==maxnum:
        print(str(i)+' ')    
