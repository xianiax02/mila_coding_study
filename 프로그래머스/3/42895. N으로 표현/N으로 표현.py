from collections import defaultdict
def solution(N, number):
    d=defaultdict(set)
    d[1].add(N)
    for i in range(2,9):
        for k in range(1,i):
            for op1 in d[k]:
                for op2 in d[i-k]:
                    d[i].add(op1+op2)
                    d[i].add(op1-op2)
                    d[i].add(op1*op2)
                    if op2:
                        d[i].add(op1//op2)
        d[i].add(int(str(N)*i))
    answer = 0
    for i in range(1,9):
        if number in d[i]:
            answer=i
            break
    
    if answer==0:
        answer=-1
    return answer