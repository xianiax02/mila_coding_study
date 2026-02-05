from collections import deque
def solution(begin, target, words):
    def adjacent(a,b):
        cnt=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                cnt+=1
            if cnt>1:
                return False
        return True
    n=len(words)
    adlist=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if adjacent(words[i],words[j]):
                adlist[i].append(j)
                adlist[j].append(i)
    answerlist=[]
    startpoints=[]
    startpoint,endpoint=n,n
    answer = 2
    for i in range(n):
        if adjacent(begin,words[i]):
            if begin==words[i]:
                startpoint=i
                answer-=1
            else:
                startpoints.append(i)
        if target==words[i]:
            endpoint=i
            answer-=1
    if startpoint!=n:
        startpoints=[startpoint]
    if endpoint==n:
        return 0
    for start in startpoints:
        visited=[0]*n
        mq=deque()
        mq.append(start)
        visited[start]=1
        while mq:
            c=mq.popleft()
            if c==endpoint:
                break
            for nxt in adlist[c]:
                if not visited[nxt]:
                    mq.append(nxt)
                    visited[nxt]=visited[c]+1
        answerlist.append(answer+visited[c]-1)
    return min(answerlist)