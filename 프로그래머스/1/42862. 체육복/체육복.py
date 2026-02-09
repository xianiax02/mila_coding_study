def solution(n, lost, reserve):
    realreserve=[]
    reallost=set(lost)
    for r in reserve:
        if  r not in lost:
            realreserve.append(r)
        else:
            reallost.remove(r)
    realreserve.sort()
    for r in realreserve:
        if r-1 in reallost:
            reallost.remove(r-1)
        elif r+1 in reallost:
            reallost.remove(r+1)
    answer = n-len(reallost)
    return answer