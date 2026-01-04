from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write
n,m,k,x=map(int,input().strip().split())
mq=deque()
visited=[-1]*(n+1) #노드 갯수 만큼 visited 배열 생성, 0 padding
graph=[ [] for _ in range(n+1)] #이것도 전체 리스트를 순회하지 않을 거니까 0 padding 가능
#인접 리스트 생성
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) #유방향이므로 하나에만 넣기
#시작 노드는 거리 기록
#visited 배열에 x로부터의 거리도 기록할 것
visited[x]=0
mq.append(x)
while mq:
   currentnode=mq.popleft()
   for nextnode in graph[currentnode]:
       if visited[nextnode]==-1: #not visited
           mq.append(nextnode)
           visited[nextnode]=visited[currentnode]+1
if visited.count(k)==0:
    print('-1')
else:
    for i in range(1,n+1):
        if visited[i]==k:
            print(str(i)+'\n')