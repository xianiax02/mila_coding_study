import heapq
import sys
input=sys.stdin.readline
v,e,k=map(int,input().split())
heap=[]
inf=float("inf")
distance=[[]*k for _ in range(1+v)] #각 거리에 k크기의 minheap 저장
graph=[[] for _ in range(v+1)] #0-padding
for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))

heapq.heappush(distance[1],0)
heapq.heappush(heap,(0,1)) 
while heap:
    mindist,minnode=heapq.heappop(heap)
    for nextnode,w in graph[minnode]:
        if len(distance[nextnode])<k:
            heapq.heappush(distance[nextnode],(-1*(mindist+w)))
            heapq.heappush(heap,((mindist+w),nextnode)) #여기서 heappush까먹음
        elif -1*(distance[nextnode][0]) > mindist+w :
            heapq.heappop(distance[nextnode])
            heapq.heappush(distance[nextnode],(-1*(mindist+w)))  #heappush로만 값을 넣었다면 리스트 자체가 이미 heap 되어있음. append 쓰지않고 heappush만 쓸걸 명심
            heapq.heappush(heap,((mindist+w),nextnode))
for i in range(1,v+1):
    if len(distance[i])!=k:
        print(-1)
    else:
        print(-1*heapq.heappop(distance[i]))