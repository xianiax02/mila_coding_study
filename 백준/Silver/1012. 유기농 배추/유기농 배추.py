import sys
from collections import deque

# Python의 재귀 깊이 제한을 늘려줍니다. BFS에서는 필수는 아니지만, 
# DFS로 풀 경우를 대비한 좋은 습관입니다.
sys.setrecursionlimit(10**6)

def bfs(start_x, start_y, m, n, farm, visited):
    """
    하나의 연결된 배추 그룹을 모두 방문 처리하는 함수 (BFS)
    """
    # 큐를 생성하고 시작점을 추가합니다.
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    # 상, 하, 좌, 우 네 방향을 검사하기 위한 리스트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 농장 범위를 벗어나지 않는지 확인
            if 0 <= nx < m and 0 <= ny < n:
                # 2. 해당 위치에 배추가 있고 아직 방문하지 않았는지 확인
                if farm[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 테스트 케이스의 수
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # m: 가로 길이, n: 세로 길이, k: 배추의 개수
    # map의 결과는 바로 변수에 할당할 수 있으므로 list()로 감쌀 필요가 없습니다.
    m, n, k = map(int, sys.stdin.readline().strip().split())
    
    # 농장과 방문 기록을 저장할 2차원 리스트 생성
    farm = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    
    # 배추 위치 입력받기
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[x][y] = 1
        
    worm_count = 0
    # 농장 전체를 순회
    for i in range(m):
        for j in range(n):
            # 만약 어떤 위치에 배추가 있고 아직 방문하지 않았다면
            if farm[i][j] == 1 and not visited[i][j]:
                # 새로운 배추 그룹을 찾았으므로 지렁이 수 증가
                worm_count += 1
                # BFS를 호출하여 이 그룹에 속한 모든 배추를 방문 처리
                bfs(i, j, m, n, farm, visited)
                
    # 결과 출력
    # sys.stdout.write는 문자열만 인자로 받으므로 str() 변환과 '\n' 추가가 필요합니다.
    # print()는 더 간편합니다.
    print(worm_count)
