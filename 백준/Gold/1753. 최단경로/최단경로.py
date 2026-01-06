import sys
import heapq
input=sys.stdin.readline
inf=float('inf')
v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range(v+1)] #0-padding
for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))
heap=[]#0-padding 힙을 쓰기 위해 노드 정보도 포함시킴
heapq.heappush(heap,(0,start))
distance=[inf]*(1+v)
distance[start]=0
#visited=[False]*(1+v)
#visited[0]=True #visited가 사실상 거리가 inf 냐 아니냐로 판단이 가능.
while heap: #visited를순차적으로 배열하지 않기 위해 존재여부로 while 문 생성 -> 하나씩 없어지는 자료구조를 활용해야함.
    mindist,minnode=heapq.heappop(heap)
    if distance[minnode]>= mindist: #지금 탐색하는게 더 짧은 거리일 경우 
        for nextnode,w in graph[minnode]:
            temp=distance[nextnode]
            distance[nextnode]=min(distance[minnode]+w,distance[nextnode])
            if distance[nextnode]!=temp:
                heapq.heappush(heap,(distance[nextnode],nextnode))

for dist in range(1,v+1):
    if distance[dist]==inf:
        print('INF')
    else:
        print(distance[dist])

