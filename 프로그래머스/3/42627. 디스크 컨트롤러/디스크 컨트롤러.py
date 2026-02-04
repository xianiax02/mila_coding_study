import heapq
def solution(jobs):
    jobs.sort(key= lambda x:x[0])
    mq=[]
    n=len(jobs)
    returntime=[0]*n
    time=0
    p=0
    taskdone=0
    cnt=0
    while cnt<n:
        while p<n and time==jobs[p][0]: #if currenttime is over next requested time #두개가 동시에들어오는 경우 고려 못함, if가 아니라 while
            heapq.heappush(mq,(jobs[p][::-1]+[p])) #add the tasknum in the list #우선순위 설정 놓침
            p+=1
        if time>=taskdone:
            if mq:
                ctasktime,crequesttime,ctasknum=heapq.heappop(mq)
                taskdone=time+ctasktime
                returntime[ctasknum]=taskdone-crequesttime
                cnt+=1
        time+=1
    answer = int(sum(returntime)/n)
    return answer