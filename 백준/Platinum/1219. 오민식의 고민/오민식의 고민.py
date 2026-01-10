import sys
from collections import deque
input=sys.stdin.readline
v,start,end,e=map(int,input().split())
graph=[]
bfsgraph=[[] for _ in range(v)]

inf=sys.maxsize
earnedmoney=[inf]*(v)
for _ in range(e):
    a,b,w=map(int,input().split())
    graph.append((a,b,w)) #tuple() 은 인자 하나만 받음
    bfsgraph[a].append((b,w))
maxmoneyearn=tuple(map(int,input().split())) # should time -1 when using it
earnedmoney[start]=-maxmoneyearn[start] #거리가 아니므로 해당도시에서벌 수 있는 돈으로 초기화.

for _ in range(v-1):
    for i in range(e):
        st,ed,w=graph[i]
        if earnedmoney[st]!=inf and earnedmoney[ed]>earnedmoney[st]+w-maxmoneyearn[ed] :            
            earnedmoney[ed]=earnedmoney[st]+w-maxmoneyearn[ed]

cycle=False
'''
for i in range(e):
    st,ed,w=graph[i]
    if ed==end and earnedmoney[ed]>earnedmoney[st]+w-maxmoneyearn[ed]:
        cycle=True  #중간에 목적지를 끼지 않는 무한 사이클이 결국 목적지에 영향을 줄때를 파악하지 못함
'''
#그럼 그냥 한번 더 실행해서 만약 end값이 달라지면  cycle=True
#for _ in range(v-1): #무한 사이클의 값이 end까지 전파될때 를 노린다. 얼마나 반복해야 전파가 가능할까? 정말 길어도 start와 end 사이에는 
#노드가 최대 v-1개 여야 하는데...
for i in range(e): #v로 잘못 넣음.
    st,ed,w=graph[i]
    if earnedmoney[st]!=inf and earnedmoney[ed]>earnedmoney[st]+w-maxmoneyearn[ed] :            
            #cycle이 확인됐으므로 이 cycle이 end와 연결되어있는지 확인
            if st==end:
                cycle=True
                break
            mq=deque()
            mq.append(st)
            visited=[False]*v
            visited[st]=True
            while mq:
                currentnode=mq.popleft()
                for nextnode,w in bfsgraph[currentnode]:
                    if not visited[nextnode]:
                        if nextnode==end: #막상 st==end일 경우가 엣지케이스가 됨. 
                            cycle=True
                            break
                        mq.append(nextnode)
                        visited[nextnode]=True
            #break #갱신되면 안됨. 같은 배열 쓸것이므로
    if cycle:
        break
            


if earnedmoney[end]==inf:
    print('gg')
elif cycle:
    print('Gee') #if elif 조건 순서 주의 
else:
    print(-earnedmoney[end])