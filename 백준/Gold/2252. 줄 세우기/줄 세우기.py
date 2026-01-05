import sys
from collections import deque
mq=deque()
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[]for _ in range(n+1)] #0-padding
indegree=[0]*(n+1) #0padding
indegree[0]=-1
result=[]
#visited=[False]*(n+1)
#visited[0]=True

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1,n+1):
    if indegree[i]==0:
        mq.append(i)
    
while mq:
    currentnode=mq.popleft()    
    result.append(currentnode)
    #visited[currentnode]=True
    for nextnode in graph[currentnode]:
        indegree[nextnode]-=1
        if indegree[nextnode]==0 : #0진입차수가 0이 된다는 것은 곳 이 노드를 가리키는 노드가 더 이상 없다는 뜻이므로 중복으로 방문여지 x
            mq.append(nextnode)
                    

print(*result)
                
                
