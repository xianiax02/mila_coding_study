from collections import deque
def solution(s):
    answer = True
    mq=deque()
    for letter in s:
        if letter=='(':
            mq.append(letter)
        elif letter==')':
            if not mq:
                return False
            else:
                mq.pop()
    if mq:
        return False
    
    return True