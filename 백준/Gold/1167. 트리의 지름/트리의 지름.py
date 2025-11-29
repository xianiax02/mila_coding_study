import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
visited=[0]*(n+1)
graph=[[]for _ in range(n+1)] #1base indexing
distance1=[0]*(n+1)
distance2=[0]*(n+1)
for _ in range(n):
    numbers=list(map(int,input().split()))
    i=1
    node=numbers[0]
    while numbers[i]!=-1:
        graph[node].append((numbers[i],numbers[i+1]))
        i+=2

mq=deque()
ans=0
#시작점에서 최대로 가는 max 노드를 찾는다. 
startnode=1
mq.append(startnode)
visited[startnode]=1
while mq:
    current=mq.popleft()
    for nextnode,weight in graph[current]:
        if not visited[nextnode]:
            mq.append(nextnode)
            distance1[nextnode]=distance1[current]+weight
            visited[nextnode]=1
furthestnode=distance1.index(max(distance1))
visited=[0]*(n+1)
mq.append(furthestnode)
visited[furthestnode]=1
while mq:
    current=mq.popleft()
    for nextnode,weight in graph[current]:
        if not visited[nextnode]:
            mq.append(nextnode)
            distance2[nextnode]=distance2[current]+weight
            visited[nextnode]=1
print(str(max(distance2)))
        
    