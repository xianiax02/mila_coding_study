from collections import deque
def solution(bridge_length, weight, truck_weights):
    mq=deque(truck_weights)
    bridge=deque([0]*bridge_length)
    bridgeweight=0
    answer = 0
    while mq or bridge:
        answer+=1
        bridgeweight-=bridge.popleft()
        if mq:
            if bridgeweight+mq[0]<=weight:
                car=mq.popleft()
            else:
                car=0
            bridgeweight+=car
            bridge.append(car)
    return answer