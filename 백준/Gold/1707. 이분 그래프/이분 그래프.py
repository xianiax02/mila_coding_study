import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
t=int(input())
#결국은 사이클 유무를 점검하는 것
for _ in range(t):
    partition=True
    v,e=map(int,input().split())
    visited=[0]*(v+1) #0 padding
    graph=[[] for _ in range(v+1)] #0 padding
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a) # no direction
    mq=deque()
    for startnode in range(1,v+1): #start with node1
        if not visited[startnode]:
            mq.append(startnode)
            visited[startnode]=1 #1팀으로 시작 -1 곱하면서 1팀 -1팀 으로 나눌 것. 
            level=0
            while mq:
                currentnode=mq.popleft()
                level+=1
                for nextnode in graph[currentnode]:
                    if visited[currentnode]==visited[nextnode]:
                        partition=False
                    if not visited[nextnode]:
                        mq.append(nextnode)
                        visited[nextnode]=visited[currentnode]*(-1)
                if not partition:
                    break
            if not partition:
                break
    if not partition:
        print('NO\n') 
    else:
        print('YES\n') 