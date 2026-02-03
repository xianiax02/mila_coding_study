from collections import deque,Counter
def solution(n, edge):
    adlist=[[] for _ in range(1+n)]
    for e in edge:
        a,b=e
        adlist[a].append(b)
        adlist[b].append(a)
    visited=[False]*(1+n)
    levels=[0]*(1+n)
    #1번 부터 시작
    mq=deque()
    mq.append(1)
    visited[1]=True
    while mq:
        c=mq.popleft()
        for nxt in adlist[c]:
            if not visited[nxt]:
                levels[nxt]=levels[c]+1
                visited[nxt]=True
                mq.append(nxt)
    counter=Counter(levels)
    answer=counter[max(levels)]
    return answer