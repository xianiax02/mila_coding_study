import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, N + 1):
    graph[i].sort()

def dfs(start_node):
    visited_dfs[start_node] = True
    print(start_node, end=' ')
    for neighbor in graph[start_node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        
        for neighbor in graph[current_node]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = True

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
print()
bfs(V)