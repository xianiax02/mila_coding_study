import heapq
from collections import deque
def solution(plans):
    answer = []
    n=len(plans)
    stoplist=deque()
    mq=[]
    convert=lambda x: int(x[0])*60+int(x[1])
    
    for i,plan in enumerate(plans):
        time=convert(plan[1])
        heapq.heappush(mq,(convert(list(plan[1].split(':'))),int(plan[2]),plan[0])) #시작시간, 소요시간, 과목이름
    prevtime,prevname=0,''
    while mq:
        if prevtime>mq[0][0]: #앞일이 끝나는 시간이 지금 시작하려는 시간보다 느릴때 우선 stoplist에 넣는다
            stoplist.append((mq[0][0],prevtime-mq[0][0],prevname))
        elif stoplist and prevtime<mq[0][0]: #앞일이 일찍 끝나고 중지시킨 일이 있을때 중지시킨 일을 집어넣는다.
            while stoplist and prevtime<mq[0][0]:
                answer.append(prevname)
                _,spendtime,name=stoplist.pop()
                prevtime+=spendtime
                prevname=name
            continue
        else: #딱맞게 끝날때 + 일찍 끝나고, stoplist가 없을때 완료 표시후, mq 빼면서 값들 갱신
            if prevname:
                answer.append(prevname)
        starttime,spendtime,name=heapq.heappop(mq)
        prevtime,prevname=starttime+spendtime,name
    answer.append(prevname) #마지막 탈출 이후 저장해주기.
    while stoplist:
        _,spendtime,name=stoplist.pop()
        answer.append(name)
    
    return answer