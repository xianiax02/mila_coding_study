from collections import deque
n,k=map(int,input().split())
mq=deque()
mq.append(n)
inf=float('inf')
max_num=100000
distance=[inf]*(max_num+1)
distance[n]=0
while mq:
    c=mq.popleft()
    if c==k:
        print(distance[c])
        break
    nextlist=[2*c,c+1,c-1]
    for nxt in nextlist:
        if -1<nxt<=max_num:
            if nxt==2*c and c!=0:
                if distance[nxt]>distance[c]:
                    mq.appendleft(nxt)
                    distance[nxt]=distance[c]
            else:
                if distance[nxt]>distance[c]+1:
                    mq.append(nxt)
                    distance[nxt]=distance[c]+1