from collections import Counter
def solution(participant, completion):
    p=dict()
    for pa in participant:
        p[pa]=p.get(pa,0)+1
    for co in completion:
        p[co]-=1
    for ans,pa in p.items():
        if pa==1:
            answer=ans
    return answer