def solution(sequence, k):
    p1,p2=0,0
    s=sequence[0]
    cands=[]
    n=len(sequence)
    while p1<=p2<n:
        if s<k and p2<n-1:
            p2+=1
            s+=sequence[p2]
        else:
            if s==k:
                cands.append((p2-p1,p1,p2))
            s-=sequence[p1]
            p1+=1
    cands.sort()
    answer = cands[0][1:]
    return answer