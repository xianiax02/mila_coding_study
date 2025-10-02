import sys
from collections import deque

# --- 입력 처리 속도를 높이기 위한 설정 ---
# input = sys.stdin.readline # 주석 해제하여 사용할 수 있습니다.

# --- 너비 우선 탐색(BFS) 함수 정의 ---
# a: x좌표(열), b: y좌표(행)
def BFS(a, b, visited, farm, m, n):
    # 상, 하, 좌, 우 이동 방향
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque()
    queue.append([a, b])
    visited[b][a] = 1 # 방문 처리: visited[행][열] = visited[y][x]
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 농장 범위를 벗어나지 않는지 확인
            if 0 <= nx < m and 0 <= ny < n:
                # 2. 해당 위치에 배추가 있고 아직 방문하지 않았는지 확인
                if farm[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append([nx, ny])

# --- 메인 로직 ---
# 테스트 케이스 수 입력
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # m: 가로 길이(열의 개수), n: 세로 길이(행의 개수), k: 배추 개수
    # .split(' ') 대신 .split()을 사용하면 여러 공백에도 안전합니다.
    m, n, k = map(int, sys.stdin.readline().strip().split())
    
    # 농장 생성 (n행 m열)
    farm = [[0] * m for _ in range(n)]
    
    # 배추 위치 입력받아 농장에 표시
    for _ in range(k):
        # list()로 감싸는 것은 불필요하지만, 원본 코드 로직을 유지했습니다.
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1 # farm[행][열] = farm[y][x]
        
    # 방문 기록을 위한 배열 생성 (n행 m열)
    visited = [[0] * m for _ in range(n)]
    worm = 0
    
    # 농장 전체를 순회 (i: 행, j: 열)
    for i in range(n):
        for j in range(m):
            # 배추가 있고 아직 방문하지 않았다면
            if (not visited[i][j]) and (farm[i][j] == 1):
                # BFS를 호출하여 연결된 모든 배추를 방문 처리
                BFS(j, i, visited, farm, m, n) # BFS에는 (x, y) 순서로 전달
                worm += 1 # 필요한 지렁이 수 증가
                
    # 결과 출력
    sys.stdout.write(str(worm) + '\n')
