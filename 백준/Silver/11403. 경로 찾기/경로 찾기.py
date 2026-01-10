#모든 노드에 관해 --> 플로이드 워셜로 전체를 한번에 구해야함. 
import sys
input=sys.stdin.readline

v=int(input())
graph=[]
for _ in range(v):
    graph.append(list(map(int,input().split())))

for k in range(v):
    for s in range(v):
        for e in range(v):
            graph[s][e]=max(graph[s][e],graph[s][k]*graph[k][e]) #둘다 1이어서 연결될때만 1이 됨. 근데 이러면 k=e일때 연결된게 비연결 처리됨. 
                #입력과 출력 예시를 보니 s=e는 기본적으로 0이고 다른 걸 거쳐서 돌아올 수 있을때 1로 바꿔주면 됨. 
                #본의 아니게 원래 1인걸 0으로 바꾸는 경우는 주의 max 쓰면 조건문 굳이 필요없음.
for i in range(v):
    print(*graph[i])
