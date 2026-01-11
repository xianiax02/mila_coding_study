from collections import deque
import sys
input=sys.stdin.readline
n=int(input())

parent=list(map(int,input().split()))
graph=[[] for _ in range(n)]
childnum=[0]*n

for child in range(n):
    parentnode=parent[child]
    if parentnode!=-1: #-1인경우 마지막 인덱스에 접근하게 되는 것 유의    
        graph[parentnode].append(child)
        childnum[parentnode]+=1

deletenode=int(input())
if parent[deletenode]!=-1:    
    childnum[parent[deletenode]]-=1
    mq=deque()
    mq.append(deletenode)
    childnum[deletenode]=-1
    while mq:
        current=mq.popleft()
        childnum
        for nextnode in graph[current]:
            mq.append(nextnode)
            childnum[nextnode]=-1
    cnt=0
    for num in childnum:
        if num==0:
            cnt+=1

    print(cnt)
else: #엣지 케이스 고려해야함.
    #root를 삭제
    print(0)

        
