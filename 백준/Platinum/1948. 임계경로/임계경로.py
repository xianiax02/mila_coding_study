#마지막에 입력되는 한걸음 부터 로마까지의 경로(가중치 합)의 최댓값과, 그 최댓값을 가진 경로의 모든 간선의 갯수를 구하는 것
# 두 지점사이의 경로를 모두 탐색
from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
mq=deque()
indegree=[0]*(1+n)
road=[0]*(1+n)
graph=[[] for _ in range(n+1)]
backgraph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append((b,w)) #상대노드와 가중치를 튜플로 저장 -> 애초에 단방향 그래프
    backgraph[b].append((a,w))
    indegree[b]+=1
start,end=map(int,input().split())
for i in range(1,n+1):
    if indegree[i]==0:
        mq.append((i,0)) #초기 진입 노드는 모두 가중치 0
while mq: #초기 진입노드==모든 경로의 출발점
#마찬가지로 도로세는건 게임 개발 문제처럼 나중가서 해야함. 시점이 다름. 그리고 어차피 어디로 가든 로마로 가기 떄문에 종점 체크할 필요가 없음.
    (currentnode,weight)=mq.popleft()
    for nextnode,w in graph[currentnode]:
        indegree[nextnode]-=1
        road[nextnode]=max(w+road[currentnode],road[nextnode]) #road에 각지점까지의 최대 거리를 저장
        if indegree[nextnode]==0:
            mq.append((nextnode,w))
bfsq=deque()
visited=[False]*(1+n)
bfsq.append((end,0))
visited[end]=True
cnt=0
while bfsq:
    currentnode,weight=bfsq.popleft()
    for previousnode,w in backgraph[currentnode]:
        if road[currentnode]==road[previousnode]+w :
            cnt+=1 #경로를 세는 것과 탐색을 하는 것은 다름을 주의             
            if not visited[previousnode]:
                visited[previousnode]=True #없어도 되지만, visited를 쓰는게 중복 탐색을 막아줘서 더 빠름.
                bfsq.append((previousnode,w))  #append는 원소 하나만 넣을 수 있음.

maxroad=road[end]
print(maxroad)
print(cnt)