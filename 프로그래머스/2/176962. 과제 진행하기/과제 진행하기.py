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
        starttime,spendtime,name=heapq.heappop(mq)
        if prevname:
            if prevtime>starttime: #여유 없이 중단하고 다른거 시작해야하는 경우
                stoplist.append((prevtime-starttime,prevname))
            else:
                answer.append(prevname)
                gap=starttime-prevtime #다음 요청때까지 남은 시간 이 존재하는 동안, stoplist에서 최대한 빼오기
                while gap and stoplist:
                    st,na=stoplist.pop()
                    if gap>=st:
                        gap-=st
                        answer.append(na)
                    else:
                        st-=gap
                        gap=0
                        stoplist.append((st,na))
        prevtime, prevname = starttime + spendtime, name
        
    answer.append(prevname) #마지막 탈출 이후 저장해주기.
    while stoplist:
        spendtime,name=stoplist.pop()
        answer.append(name)
    
    return answer