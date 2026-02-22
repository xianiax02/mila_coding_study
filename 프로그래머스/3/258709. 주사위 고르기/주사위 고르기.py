
from itertools import combinations
from bisect import bisect_left
from functools import lru_cache
def solution(dice):
    n=len(dice)
    choices=list(combinations([i for i in range(n)],n//2))
    wins=[0]*len(choices)
    answer = []
    @lru_cache(None)
    def search(choice):
        if len(choice)==1:
            d=dict()
            for num in dice[choice[0]]:
                d[num]=d.get(num,0)+1
            return d
        d=dict()
        prev_results=search(choice[:-1])
        for s,num1 in prev_results.items():
            for num2 in dice[choice[-1]]:
                d[s+num2]=d.get(s+num2,0)+num1
        return d
    for choicenum, choice in enumerate(choices):
        a_d=search(choice)
        b_d=search(tuple(sorted(set(range(n))-set(choice))))
        b_d=sorted(b_d.items())
        b_num=[x[0] for x in b_d]
        b_sum=[b_d[0] for _ in range(len(b_d))]
        for i in range(1,len(b_d)):
            b_sum[i]=(b_d[i][0],b_sum[i-1][1]+b_d[i][1])
        ans=0
        for k,v in a_d.items():
            idx=bisect_left(b_num,k)
            if idx>0:
                ans+=b_sum[idx-1][1]*v
        wins[choicenum]=ans
    answer=list(choices[wins.index(max(wins))])
    answer=sorted([i+1 for i in answer])
    return answer