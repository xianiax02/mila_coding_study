def solution(answers):
    scorelist=[0,0,0]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    an,bn,cn,n=len(a),len(b),len(c),len(answers)
    for i in range(n):
        aidx,bidx,cidx=i%an,i%bn,i%cn
        if a[aidx]==answers[i]:
            scorelist[0]+=1
        if b[bidx]==answers[i]:
            scorelist[1]+=1
        if c[cidx]==answers[i]:
            scorelist[2]+=1
    answer = []
    for i,s in enumerate(scorelist):
        if s==max(scorelist):
            answer.append(i+1)
    
    return answer