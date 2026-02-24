from collections import Counter
from itertools import combinations_with_replacement
def solution(n, info):
    cases=list(combinations_with_replacement([i for i in range(11)],n))
    def convert(case):
        lst=[0]*11
        counter=Counter(case)
        for i in range(11):
            lst[i]=counter[i]
        return lst
    cases=[convert(case) for case in cases]
    casenum=len(cases)
    casescores=[0]*casenum
    def getscorediff(ryan):
        peachscore=0
        ryanscore=0
        for i in range(11):
            if info[i]>=ryan[i]:
                if info[i]!=0:
                    peachscore+=10-i
            else:
                ryanscore+=10-i
        return ryanscore-peachscore
    maxscorediff=(0,[])
    cands=[]
    for i,case in enumerate(cases):
        scorediff=getscorediff(case)
        casescores[i]=scorediff
        if (scorediff,case[::-1])>maxscorediff:
            maxscorediff=(scorediff,case[::-1])
            answer=case
    if maxscorediff[0]<=0:
        return [-1] 
    return answer