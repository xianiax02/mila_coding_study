import sys
from collections import deque

# sys.stdin.readline()을 사용하기 위해 import
# input = sys.stdin.readline # 이렇게 맨 위에 선언해두면 기존 코드를 바꿀 필요 없이 편리합니다.

sys.setrecursionlimit(10**6)

# input() 대신 sys.stdin.readline() 사용
N, M = map(int, sys.stdin.readline().split()) 
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # 여기도 마찬가지로 변경
    u, v = map(int, sys.stdin.readline().split()) 
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 이 DFS 함수는 현재 코드에서 사용되고 있지는 않지만, 로직은 올바릅니다.
def dfs(start_node):
    visited[start_node] = True
    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            dfs(neighbor)

component_count = 0

for i in range(1, N + 1):
    if not visited[i]:
        # 새로운 연결 요소를 발견하면 BFS(너비 우선 탐색) 실행
        bfs(i) 
        component_count += 1

print(component_count)