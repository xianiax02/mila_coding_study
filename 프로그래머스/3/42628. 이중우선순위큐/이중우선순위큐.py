import heapq

def solution(operations):
    max_h, min_h = [], []
    # 각 연산 인덱스별로 '생존 여부'를 체크하는 배열
    visited = [False] * len(operations)
    
    for i, op in enumerate(operations):
        cmd, val = op.split()
        num = int(val)
        
        if cmd == 'I':
            heapq.heappush(min_h, (num, i))   # (값, 고유ID)
            heapq.heappush(max_h, (-num, i)) # (-값, 고유ID)
            visited[i] = True               # i번 데이터 생존!
            
        elif num == 1: # 최댓값 삭제
            # 1. 쓰레기 데이터 정리 (이미 다른 쪽에서 삭제된 놈들)
            while max_h and not visited[max_h[0][1]]:
                heapq.heappop(max_h)
            # 2. 진짜 삭제
            if max_h:
                visited[max_h[0][1]] = False
                heapq.heappop(max_h)
        else: # 최솟값 삭제
            while min_h and not visited[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                visited[min_h[0][1]] = False
                heapq.heappop(min_h)

    # 마지막 결과 출력 전에도 한 번 더 청소
    while min_h and not visited[min_h[0][1]]: heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]: heapq.heappop(max_h)

    if not min_h:
        return [0, 0]
    return [-max_h[0][0], min_h[0][0]]