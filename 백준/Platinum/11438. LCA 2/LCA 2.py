import sys
from collections import deque

# 1. 빠른 입출력 설정
input = sys.stdin.readline

def solve():
    # N 입력 처리
    line = input().strip()
    if not line: return
    n = int(line)
    
    # 인접 리스트 생성
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u) # [FIXED] 'a'라고 잘못 썼던 부분을 'u'로 수정했습니다.

    # 2. 희소 테이블(Sparse Table) 및 레벨 배열 준비
    # n.bit_length()는 n을 표현하는 데 필요한 비트 수 (최대 점프 높이)
    LOG = n.bit_length()
    parent = [[0] * (n + 1) for _ in range(LOG)]
    level = [-1] * (n + 1)

    # 3. BFS로 각 노드의 레벨과 직계 부모(2^0) 찾기
    queue = deque([1])
    level[1] = 0
    while queue:
        curr = queue.popleft()
        for nxt in adj[curr]:
            if level[nxt] == -1:
                level[nxt] = level[curr] + 1
                parent[0][nxt] = curr
                queue.append(nxt)

    # 4. 희소 테이블 구축 (DP): O(N log N)
    for k in range(1, LOG):
        for i in range(1, n + 1):
            if parent[k-1][i] != 0:
                # i의 2^k번째 조상은 (i의 2^(k-1) 조상)의 2^(k-1) 조상
                parent[k][i] = parent[k-1][parent[k-1][i]]

    # 5. LCA 쿼리 처리: O(M log N)
    m_line = input().strip()
    if not m_line: return
    m = int(m_line)
    
    results = []
    for _ in range(m):
        u, v = map(int, input().split())
        
        # 깊이 맞추기: u가 항상 더 깊도록 설정
        if level[u] < level[v]:
            u, v = v, u
        
        # 1) 레벨 차이(diff)만큼 비트 단위로 점프
        diff = level[u] - level[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                u = parent[k][u]
        
        # 레벨을 맞췄는데 같으면 그게 LCA
        if u == v:
            results.append(str(u))
            continue
            
        # 2) 조상이 다를 때만 큰 폭에서 작은 폭으로 점프
        for k in range(LOG - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        
        # 루프 종료 후 바로 위 부모가 LCA
        results.append(str(parent[0][u]))

    # 6. 한 번에 출력하여 시간 단축
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()