import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    n=len(progresses)
    daysleft=[math.ceil((100-progresses[i])/speeds[i]) for i in range(n)]
    daysleft=deque(daysleft)
    print(daysleft)
    while daysleft:
        c=daysleft.popleft()
        answer.append(1)
        while daysleft and daysleft[0]<=c:
            daysleft.popleft()
            answer[-1]+=1
    return answer