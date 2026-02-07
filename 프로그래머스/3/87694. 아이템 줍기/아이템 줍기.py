from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx,dy=[-1,0,1,0],[0,-1,0,1]
    visited=[[0]*101 for _ in range(101)]
    maps=[[0]*101 for _ in range(101)]
    for (nx,ny,xx,xy) in rectangle:
        for x in range(2*nx,2*(xx)+1):
            for y in range(2*ny,2*(xy)+1):
                maps[x][y]=1
    for (nx,ny,xx,xy) in rectangle:
        for x in range(2*(nx)+1,2*(xx)):
            for y in range(2*(ny)+1,2*(xy)):
                maps[x][y]=0
    mq=deque()
    mq.append((2*characterX,2*characterY))
    while mq:
        cx,cy=mq.popleft()
        if (cx,cy)==(2*itemX,2*itemY):
            break
        for d in range(4):
            nx,ny=cx+dx[d],cy+dy[d]
            if (nx,ny)==(2*characterX,2*characterY):
                continue
            if (-1<nx<101 and -1<ny<101) and (not visited[nx][ny]) and (maps[nx][ny]==1):
                visited[nx][ny]=visited[cx][cy]+1
                mq.append((nx,ny))
    
    answer = visited[2*itemX][2*itemY]//2
    return answer