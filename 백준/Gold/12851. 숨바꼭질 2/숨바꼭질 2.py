import sys
from collections import deque
n,k=map(int,sys.stdin.readline().strip().split(' '))
if n >= k:
    print(n - k) # 가장 빠른 시간: 뒤로 가는 시간
    print(1)     # 방법의 수: 1가지
    sys.exit()
dist=[-1]*100001
queue=deque()
fastesttime=99999
routenums=0
queue.append((n,0))
dist[n]=0
while queue:
    a,level=queue.popleft() 
    if fastesttime!=99999 and dist[a]>= fastesttime:
        continue
    for nextpos in (a-1,a+1,a*2):
        if 0<=nextpos<100001:
            if dist[nextpos]==-1 or (dist[nextpos]==dist[a]+1) : #미방문한 노드, 또는 바로 전단계 보다 빠르게 횟수로 방문하는 노드일시 큐에 넣기
                if nextpos==k:
                    fastesttime=min(fastesttime,level+1)
                    routenums+=1 #경로를 찾은 것
                else:
                    queue.append((nextpos,level+1))
                    dist[nextpos]=dist[a]+1   #거리 갱신해주기 
                
sys.stdout.write(str(fastesttime)+'\n')               
sys.stdout.write(str(routenums)+'\n')