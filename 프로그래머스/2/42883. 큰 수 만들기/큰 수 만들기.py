from collections import deque
def solution(numbers, k):
    numbers=[int(x) for x in numbers]
    cnt=0
    mq=deque()
    n=len(numbers)
    for number in numbers:
        while mq and mq[-1]<number and cnt<k:
            mq.pop()
            cnt+=1
        mq.append(number)
    while len(mq)>n-k:
        mq.pop()
    answer = ''.join([str(x) for x in list(mq)])
    return answer