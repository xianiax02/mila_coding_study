def solution(brown, yellow):
    answer = []
    cands=[]
    t=brown+yellow
    n=int(t**(1/2))+1
    for a in range(3,n):
        if t%a==0:
            cands.append(a)
    for cand in cands:
        b=t//cand
        supposey=(cand-2)*(b-2)
        supposeb=cand*b-supposey
        if (supposey,supposeb)==(yellow,brown):
            answer.append(b)
            answer.append(cand)
            break
    
    return answer