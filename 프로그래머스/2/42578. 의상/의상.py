def solution(clothes):
    clothset=dict()
    for cloth in clothes:
        clothset[cloth[1]]=clothset.get(cloth[1],[])+[cloth[0]]    
    answer = 1
    for category,clist  in clothset.items():
        answer*=(len(clist)+1)

    return answer-1