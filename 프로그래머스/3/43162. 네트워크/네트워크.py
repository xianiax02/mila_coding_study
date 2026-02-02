from collections import deque
def solution(n, computers):
    answer = 0
    visited=[False]*n
    adlist=[[] for _ in range(n)]
    for index in range(n):
        for ad in range(n):
            if computers[index][ad]==1 and index!=ad:
                adlist[index].append(ad)
    for a in range(n): #각 노드에서 방문하지 않은 것에 대해 탐색시도
        if not visited[a]:
            answer+=1
            mq=deque()
            mq.append(a)
            visited[a]=True
            while mq:
                c=mq.popleft()
                for n in adlist[c]:
                    if not visited[n]:
                        mq.append(n)
                        visited[n]=True
    return answer