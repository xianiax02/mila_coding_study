import heapq
def solution(jobs):
    waitlist=[]
    joblist=[]
    n=len(jobs)
    returntime=[0]*n
    for jobnum,job in enumerate(jobs):
        rt,st=job #requesttime,spendtime
        joblist.append((st,rt,jobnum))
    joblist.sort(key=lambda x: x[1])
    time=0
    cnt=0
    p=0
    workdone=0
    while cnt<n:
        while p<n and time>=joblist[p][1]:
            heapq.heappush(waitlist,joblist[p])
            p+=1
        if waitlist and workdone<=time:
            st,rt,jobnum=heapq.heappop(waitlist)
            cnt+=1
            workdone=time+st
            returntime[jobnum]=workdone-rt
        time+=1
    answer = sum(returntime)//n
    return answer