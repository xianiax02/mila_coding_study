from collections import deque
def solution(maps):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    answer=[]
    m,n=len(maps),len(maps[0])
    visited=[[False]*n for _ in range(m)]
    mq=deque()
    for i in range(m):
        for j in range(n):
            island=0
            if not visited[i][j] and maps[i][j]!='X':
                mq.append((i,j))
                visited[i][j]=True
                while mq:
                    ci,cj=mq.popleft()
                    island+=int(maps[ci][cj])
                    for d in range(4):
                        ni,nj=ci+dx[d],cj+dy[d]
                        if not (-1<ni<m and -1<nj<n) :
                            continue
                        if not visited[ni][nj] and maps[ni][nj]!='X':
                            mq.append((ni,nj))
                            visited[ni][nj]=True
                answer.append(island)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer