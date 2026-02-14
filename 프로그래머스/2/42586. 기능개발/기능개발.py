import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    n=len(progresses)
    daysleft=[-(-(100-progresses[i])//speeds[i]) for i in range(n)]
    maxday=-1
    for i in daysleft:
        if maxday>=i:
            answer[-1]+=1
        else:
            maxday=i
            answer.append(1)
    return answer