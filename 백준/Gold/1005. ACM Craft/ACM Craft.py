import sys
input=sys.stdin.readline 
from collections import deque
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    required=[0]+list(map(int,input().split()))
    answer=[0]*(1+n)
    indegree=[0]*(1+n)
    adlist=[[] for _ in range(n+1)] #n-1번 건물로
    for _ in range(k):
        a,b=map(int,input().split())
        adlist[a].append(b)
        indegree[b]+=1
    goal=int(input())
    mq=deque()
    for i,num in enumerate(indegree):
        if num==0 and i!=0:
            mq.append(i)
            answer[i]=required[i]
    
    while mq:
        c=mq.pop()
        for nxt in adlist[c]:
            answer[nxt]=max(answer[c]+required[nxt],answer[nxt])
            indegree[nxt]-=1
            if not indegree[nxt]:
                mq.append(nxt)
    print(answer[goal])