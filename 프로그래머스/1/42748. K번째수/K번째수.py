import bisect

def solution(array, commands):
    n = len(array)
    # 1. 트리 초기화 (충분한 크기의 공간 확보)
    tree = [[] for _ in range(4 * n)]
    
    # 2. 트리 빌드 함수 (Recursive Build)
    def build(node, start, end):
        if start == end:
            tree[node] = [array[start]]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        # 자식 노드들을 합치며 정렬 (Merge)
        tree[node] = sorted(tree[2 * node] + tree[2 * node + 1])

    # 3. 구간 쿼리 함수 (val보다 작은 숫자의 개수 반환)
    def query(node, start, end, l, r, val):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            # 이진 탐색으로 val보다 작은 원소의 개수를 O(log N)에 찾음
            return bisect.bisect_left(tree[node], val)
        mid = (start + end) // 2
        return query(2 * node, start, mid, l, r, val) + \
               query(2 * node + 1, mid + 1, end, l, r, val)

    # 실행: 트리 생성
    build(1, 0, n - 1)
    
    # 이분 탐색을 위해 전체 배열 정렬본 준비
    sorted_unique = sorted(array)
    answer = []

    # 4. 각 명령 처리
    for i, j, k in commands:
        l, r = i - 1, j - 1
        low, high = 0, len(sorted_unique) - 1
        res = 0
        
        # 'K번째 수'를 찾기 위한 값의 이분 탐색 (Binary Search on Values)
        while low <= high:
            mid = (low + high) // 2
            val = sorted_unique[mid]
            # 구간 [l, r] 내에 val보다 작은 숫자가 몇 개 있는지 체크
            if query(1, 0, n - 1, l, r, val) < k:
                res = val
                low = mid + 1
            else:
                high = mid - 1
        answer.append(res)
        
    return answer