from collections import deque
def solution(priorities, location):
    priorities=deque(priorities)
    n=len(priorities)
    count=0
    while priorities:
        execute=True
        c=priorities.popleft()
        n-=1
        for p in priorities:
            if p>c:
                execute=False
                priorities.append(c)
                n+=1
                break
        if execute==True:
            count+=1
            if location==0 : return count
        location=(location-1)%n