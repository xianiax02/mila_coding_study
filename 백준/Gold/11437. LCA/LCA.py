from collections import deque
import sys

input = sys.stdin.readline
# print = sys.stdout.write  <- 잦은 호출 방지를 위해 아래에서 리스트로 처리합니다.

n = int(input())
linklist = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    linklist[a].append(b)
    linklist[b].append(a)

# BFS: 레벨 및 부모(2^0) 초기화
parent = [[0] * (n + 1)]
level = [-1] * (n + 1)
mq = deque([1])
level[1] = 0
visited = [False] * (n + 1)
visited[1] = True

maxlevel = 0
while mq:
    currentnode = mq.popleft()
    for nextnode in linklist[currentnode]:
        if not visited[nextnode]:
            visited[nextnode] = True
            level[nextnode] = level[currentnode] + 1
            maxlevel = max(maxlevel, level[nextnode])
            mq.append(nextnode)
            parent[0][nextnode] = currentnode

# powerlevel 계산 및 희소 테이블 구축
powerlevel = maxlevel.bit_length()
parent = parent + [[0] * (n + 1) for _ in range(powerlevel)]

for k in range(1, powerlevel + 1):
    for num in range(1, n + 1):
        if parent[k-1][num] != 0:
            parent[k][num] = parent[k-1][parent[k-1][num]]

m = int(input())
results = [] # 결과를 담아 한 번에 출력하기 위함

for _ in range(m):
    a, b = map(int, input().split())
    
    # 1. 레벨 맞추기 (비트 점프로 최적화)
    if level[a] < level[b]:
        a, b = b, a
    
    diff = level[a] - level[b]
    for k in range(powerlevel + 1):
        if (diff >> k) & 1:
            a = parent[k][a]
            
    # 2. 레벨을 맞췄는데 같다면 b가 LCA
    if a == b:
        results.append(str(a))
        continue
        
    # 3. 공통 조상 찾기 (Binary Lifting)
    for k in range(powerlevel, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
            
    results.append(str(parent[0][a]))

# 4. 전체 결과를 한 번에 출력 (Python 3에서 TLE 방지 핵심)
sys.stdout.write('\n'.join(results) + '\n')