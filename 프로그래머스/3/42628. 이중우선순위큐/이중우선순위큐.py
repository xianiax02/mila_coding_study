from bisect import bisect_left
def solution(operations):
    answer = []
    for operation in operations:
        command,num=operation.split()
        num=int(num)
        if command=='I':
            if answer:
                pos=bisect_left(answer,num)
                answer.insert(pos,num)
            else:
                answer.append(num)
        elif command=='D':
            if answer:
                if num==1:
                    answer.remove(answer[-1])
                elif num==-1:
                    answer.remove(answer[0])
    if not answer:
        answer=[0,0]
    else: answer=[answer[-1],answer[0]]
    return answer