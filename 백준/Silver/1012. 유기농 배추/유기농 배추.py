import sys
from collections import deque

def BFS(x, y, visited, farm, m, n):
    dx = [1, 0, -1, 0]   # 좌우 이동 (열 변화)
    dy = [0, 1, 0, -1]   # 상하 이동 (행 변화)
    queue = deque()
    queue.append((x, y))
    visited[y][x] = 1   # (행, 열) = (y, x)
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]   # 열
            ny = cy + dy[i]   # 행
            if 0 <= nx < m and 0 <= ny < n:
                if farm[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((nx, ny))

# 테스트 케이스 수
t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    farm = [[0] * m for _ in range(n)]       # n행(m열)
    visited = [[0] * m for _ in range(n)]    # n행(m열)

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1   # (행=y, 열=x)

    worm = 0
    for i in range(n):        # 행
        for j in range(m):    # 열
            if farm[i][j] == 1 and not visited[i][j]:
                BFS(j, i, visited, farm, m, n)   # (x=j, y=i)
                worm += 1

    sys.stdout.write(str(worm)+'\n')