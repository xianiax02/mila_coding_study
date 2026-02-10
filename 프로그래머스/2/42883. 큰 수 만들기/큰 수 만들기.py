from collections import deque
def solution(number, k):
    mq=deque()
    n=len(number)
    cnt=0
    for num in number:
        while mq and int(mq[-1])<int(num) and cnt<k :
            mq.pop()
            cnt+=1
        if (n-k)>len(mq):
            mq.append(num)
    answer=''.join(mq)
    return str(int(answer))