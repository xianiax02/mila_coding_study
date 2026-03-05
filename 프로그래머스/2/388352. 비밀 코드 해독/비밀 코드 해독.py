from itertools import combinations
def solution(n, q, ans):
    answer = 0
    candidates=[set(comb) for comb in combinations(range(1,n+1),5)]
    for candidate in candidates:
        thisisok=True
        for query,response in zip(q,ans):
            query=set(query)
            if len(candidate&query)!=response:
                thisisok=False
                break
        if thisisok:
            answer+=1
    return answer