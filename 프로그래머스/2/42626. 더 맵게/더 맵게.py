import heapq
def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while len(scoville)>1 and scoville[0]<K:
        ing1=heapq.heappop(scoville)
        ing2=heapq.heappop(scoville)
        mixed=ing1+ing2*2
        cnt+=1
        heapq.heappush(scoville,mixed)
    if scoville[0]<K:
        cnt=-1
    answer = cnt
    return answer