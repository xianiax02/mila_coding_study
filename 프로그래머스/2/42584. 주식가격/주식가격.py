from collections import deque
def solution(prices):
    mq=deque()
    n=len(prices)
    answer = [-1]*n
    for i,price in enumerate(prices) :
            while mq and mq[-1][0]>price :
                p,t=mq.pop()
                answer[t]=i-t
            mq.append((price,i))
    while mq :
        p,t=mq.pop()
        answer[t]=i-t
    return answer