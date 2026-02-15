from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    di=[-1,0,1,0]
    dj=[0,-1,0,1]
    maps=[[0]*101 for _ in range(101)]
    visited=[[0]*101 for _ in range(101)]
    for rect in rectangle:
        lbx,lby,rux,ruy=rect
        for i in range(2*lbx,2*(rux)+1):
            for j in range(2*lby,2*(ruy)+1):
                maps[i][j]=1
    for rect in rectangle:
        lbx,lby,rux,ruy=rect
        for i in range(2*lbx+1,2*(rux)):
            for j in range(2*lby+1,2*(ruy)):
                maps[i][j]=0
    mq=deque()
    mq.append((2*characterX,2*characterY))
    visited[2*characterX][2*characterY]=1
    while mq:
        ci,cj=mq.popleft()
        if (ci,cj)==(2*itemX,2*itemY):
            break
        for ddi,ddj in zip(di,dj):
            ni,nj=ci+ddi,cj+ddj
            if (-1<ni<101) and (-1<nj<101) and not visited[ni][nj] and maps[ni][nj]:
                visited[ni][nj]=visited[ci][cj]+1
                mq.append((ni,nj))        
    answer = (visited[2*itemX][2*itemY]-1)//2
    return answer