from collections import deque
import heapq
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

#그래프 순회하면서 BFS로 땅 구분하기
visited=[[False]*m for _ in range(n)] #인덱스 실수, mn바꿔씀 [m]은 왜 쓴거지?
territory=0 #바다랑 구분하려면 1부터 시작해야함. 
mq=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            territory+=1 #땅 발견 카운트하는 역할도 함.
            mq.append((i,j))
            visited[i][j]=True
            graph[i][j]=territory
            while mq:
                currenti,currentj=mq.popleft()
#                for di in [1,0,-1,0]:
#                    for dj in [0,1,0,-1]: #인접리스트 대체
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:   
                        nexti=currenti+di
                        nextj=currentj+dj
                        if 0<=nexti<n and 0<=nextj<m : #인덱스 주의. m-1까지
                            if graph[nexti][nextj] and not visited[nexti][nextj]: #바다가 아니고 방문안한 노드면
                                mq.append((nexti,nextj))
                                visited[nexti][nextj]=True
                                graph[nexti][nextj]=territory
#그래프 순회하면서 엣지 후보 정하고 heapq에 삽입하기
edges=[]
for currenti in range(n):
    for currentj in range(m):
        if graph[currenti][currentj]:
            start=graph[currenti][currentj]
            nextj=currentj+1
            nexti=currenti+1
            cntx=0
            cnty=0 #cnt 통합해서 구현해버림.
            #가로 방향 엣지
            if 0<=nextj<m: #가장자리에 있으면 pass
                while 0<=nextj<m and not graph[currenti][nextj]:
                    cntx+=1 #바다에 있다는 것 확인이 됐으니 카운트
                    nextj+=1
                if nextj<m and cntx>=2 : #멈추고 난 후 -> 끝에 도달했거나 땅을 발견했거나 도달했으면 인덱스 범위 초과
                    end=graph[currenti][nextj]
                    if end!=start:
                       heapq.heappush(edges,(cntx,start,end)) #자기에서 자기로 가는 엣지 제거해주자(사실 find 에서 걸러지긴 한다. )
            #세로 방향 엣지
            if 0<=nexti<n: #가장자리에 있으면 pass
                while 0<=nexti<n and not graph[nexti][currentj]:
                    cnty+=1 #바다에 있다는 것 확인이 됐으니 카운트
                    nexti+=1
                if nexti<n and cnty>=2 : #멈추고 난 후 -> 끝에 도달했거나 땅을 발견했거나 도달했으면 인덱스 범위 초과 cnt 조건은 바로 옆이 땅인 경우 거르기 위해
                    end=graph[nexti][currentj]
                    if end!=start:
                       heapq.heappush(edges,(cnty,start,end))
                        
#MST 구하기
rootgraph=[i for i in range(territory+1)] #[[i] for i in range(territory+1)] 이거 아님!!
result=[]
resultcnt=0
def find(x):
    if rootgraph[x]==x:
        return x
    rootgraph[x]=find(rootgraph[x])
    return rootgraph[x]

def union(a,b):
    roota=find(a)
    rootb=find(b)
    if roota!=rootb:
        rootgraph[max(roota,rootb)]=min(roota,rootb)

while edges and resultcnt!=territory-1: #결과 엣지가 v-1이 될때 종료 조건 잘 확인하기 실수
    w,s,e=heapq.heappop(edges) #heappop을 heappush로 쓰는 실수
    roots=find(s)
    roote=find(e)
    if roots!=roote:
        union(s,e)
        result.append((w,s,e))
        resultcnt+=1
#모든 섬을 연결할 수 없는 경우 고려
if resultcnt!=territory-1:
    print(-1)
else:
    ans=0
    for a in result:
        ans+=a[0]
    print(ans)
