from collections import deque
def solution(numbers):
    answer = [-1]*len(numbers)
    mq=deque()
    for i,num in enumerate(numbers):
        while mq and mq[-1][0]<num:
            a,idx=mq.pop()
            answer[idx]=num
        mq.append((num,i))
    return answer