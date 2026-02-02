def solution(nodes, edges):
    parent = {node: node for node in nodes}
    degree = {node: 0 for node in nodes}
    
    # 1. 차수 계산 및 Union-Find 준비
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i]) # 경로 압축 (Path Compression)
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # 2. 모든 간선을 합치기 (덩어리 나누기)
    for a, b in edges:
        union(a, b)

    # 3. 루트별로 타입 개수 집계
    # 결과 구조: {root_node: [type0_count, type1_count]}
    comp_stats = {}
    
    for node in nodes:
        root = find(node)
        if root not in comp_stats:
            comp_stats[root] = [0, 0]
        
        # 타입 판별 로직 (v % 2 == degree % 2 이면 Type 0)
        if node % 2 == degree[node] % 2:
            comp_stats[root][0] += 1 # Type 0 추가
        else:
            comp_stats[root][1] += 1 # Type 1 추가

    # 4. 최종 트리 개수 카운트
    h_tree, r_tree = 0, 0
    for t0, t1 in comp_stats.values():
        if t0 == 1: h_tree += 1
        if t1 == 1: r_tree += 1

    return [h_tree, r_tree]