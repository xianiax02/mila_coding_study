from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for comb in combinations(range(1,n+1),5):
        candidate=set(comb)
        thisisok=True
        for query,response in zip(q,ans):
            query=set(query)
            if len(candidate&query)!=response:
                thisisok=False
                break
        if thisisok:
            answer+=1
    return answer