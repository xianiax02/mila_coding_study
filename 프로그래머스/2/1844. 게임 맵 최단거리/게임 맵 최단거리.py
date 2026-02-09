from collections import deque
def solution(maps):
    m,n=len(maps[0]),len(maps)
    di=[-1,0,1,0]
    dj=[0,-1,0,1]
    visited=[[0]*(m) for _ in range(n)] #no padding
    mq=deque()
    mq.append((0,0))
    visited[0][0]=1 
    while mq:
        ci,cj=mq.popleft()
        for ddi,ddj in zip(di,dj):
            ni,nj=ci+ddi,cj+ddj
            if (0<=ni<n and 0<=nj<m) and not visited[ni][nj] and maps[ni][nj]:
                mq.append((ni,nj))
                visited[ni][nj]=visited[ci][cj]+1
    if visited[n-1][m-1]==0:
        return -1
    else:
        return visited[n-1][m-1]