#사람 수가 적고(100) 전체 관계를 다 알아야 하므로 플로이드 워셜 생각해 볼 수 있음.
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
inf=float('inf')
graph=[[inf]*(1+n) for _ in range(1+n)] #0-padding
for i in range(1,n+1):
    graph[i][i]=0 #자기자신은 0단계
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1 #1단계 임을 저장
    graph[b][a]=1 #1단계 임을 저장

#한번 훑을 때마다 한번씩 이어지므로, 6번 전체 인접행렬을 훑으면 됨.
#for _ in range(6): #할 필요 없음 삼중문이 모든 케이스를 한번에 계산함. 
for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if graph[s][k] and graph[k][e]: #중간에 공통으로 아는 사람이 있어야 이어진다. 
                graph[s][e]=min(graph[s][e],graph[s][k]+graph[k][e]) #min을 쓰기 때문에 inf도입, 그리고 min이 있어야 불필요하게 아는 사람 돌려서 만나는 것 방지
                graph[e][s]=graph[s][e]

#별도 배열 선언하기 힘드니 안쓰는 제로 패딩 0열에 케빈베이컨 수를 저장하자.
for i in range(1,n+1):
    graph[0][i]=sum(graph[i][1:])
    graph[i][0]=graph[0][i]

winnernumber=min(graph[0][1:])
winner=graph[0].index(winnernumber) #잘라내서 인덱스 오류 나는 것 주의.
print(winner)