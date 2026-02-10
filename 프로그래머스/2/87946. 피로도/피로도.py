from itertools import permutations
def solution(k, dungeons):
    n=len(dungeons)
    startk=k
    answer = -1
    for route in permutations(list(range(n)),n):
        count=0
        k=startk
        for dun in route:
            mink,spendk=dungeons[dun]
            if k>=mink:
                count+=1
                k-=spendk    
            else:
                break
        answer=max(answer,count)
            
    return answer