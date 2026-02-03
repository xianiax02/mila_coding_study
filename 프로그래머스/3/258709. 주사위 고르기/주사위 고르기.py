from itertools import combinations
from bisect import bisect_left
def solution(dice):
    answer = []
    maxwin=-1
    n=len(dice)
    combs=list(combinations([i for i in range(1,n+1)],n//2)) #a가 뽑는 주사위 경우의 수
    for acomb in combs:
        bcomb=[i for i in range(1,n+1) if i not in acomb]
        asum=[0]
        bsum=[0]
        awins=0
        for adicenum,bdicenum in zip(acomb,bcomb):
            temp=[]
            for s in asum:
                for i in range(6):
                    temp.append(s+dice[adicenum-1][i])
            asum=temp
            temp=[]
            for s in bsum:
                for i in range(6):
                    temp.append(s+dice[bdicenum-1][i])
            bsum=temp
        asum.sort()
        bsum.sort()
        for s in asum:
            awins+=bisect_left(bsum,s)
        if awins>maxwin:
            maxwin=awins
            answer=acomb   
    answer=sorted(list(answer))
    return answer