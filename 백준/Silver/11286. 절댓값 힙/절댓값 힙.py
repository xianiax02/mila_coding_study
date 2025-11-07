import heapq  # 1. heapq 모듈을 import
import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())

# 2. heapq는 PriorityQueue() 대신 빈 리스트[]를 사용
pq = [] 

for _ in range(n):
    num=int(input().strip())
    if num==0:
        # 3. 리스트는 'if pq:' (비어있지 않다면) 구문이 잘 작동합니다!
        if pq:
            # 4. pq.get() 대신 heapq.heappop(pq) 사용
            print(str(heapq.heappop(pq)[1])+'\n')
        else:
            print('0\n')
    else:
        # 5. pq.put() 대신 heapq.heappush(pq, ...) 사용
        heapq.heappush(pq, (abs(num), num))