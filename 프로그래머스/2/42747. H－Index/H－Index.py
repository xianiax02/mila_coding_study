
from bisect import bisect_left
def solution(citations):
    answer = 0
    n=len(citations)
    citations.sort()
    for i in range(citations[-1]+1):
        pos=bisect_left(citations,i) #i번 인용된 논문 보다 적게 인용된 논문이 pos 개. i번 이상 인용된 논문이 n-pos개   
        if i<=(n-pos):
            answer=max(answer,i)

    return answer