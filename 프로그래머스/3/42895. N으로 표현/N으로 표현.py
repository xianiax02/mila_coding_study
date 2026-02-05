def solution(N, number):
    answer = 0
    d=[set() for _ in range(9)]
    d[1].add(N)
    for i in range(2,9):
        d[i].add(int(str(N)*i))
        for j in range(1,i):
            k=i-j
            for op1 in d[j]:
                for op2 in d[k]:
                    d[i].add(op1+op2)
                    d[i].add(op1*op2)
                    d[i].add(op1-op2)
                    if op1!=0 and op2!=0:
                        d[i].add(op2//op1)
                        d[i].add(op1//op2)
    for i in range(1,9):
        if number in d[i]:
            answer=i
            break
    if answer==0:
        answer=-1
    return answer