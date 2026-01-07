import sys
import heapq
input=sys.stdin.readline
inf=float('inf')
v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)] #0-padding
heap=[]

for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))
start,end=map(int,input().split())
heapq.heappush(heap,(0,start))
distance=[inf]*(1+v)
distance[start]=0 #빼먹음
while heap:
    mindist,minnode=heapq.heappop(heap)
    if distance[minnode]>=mindist: #이미 기존에 찾은 거리가 더 가까우면 넘어가고 이번에 찾은 거리가 유의미할때만 비교진행 #등호는 맨 초기 조건 때문에 넣는 것.
        for nextnode,w in graph[minnode]:
            if mindist+w<distance[nextnode]: #if not visited 대체
                distance[nextnode]=mindist+w
                heapq.heappush(heap,(distance[nextnode],nextnode)) #지금노드 거쳐서 가는거랑 기존에 이미 구했던 거리 비교해서 짧은 걸로 계산

print(distance[end])
    

