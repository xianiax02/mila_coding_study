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
        while p<n and time>=joblist[p][1]: #실수
            heapq.heappush(waitlist,joblist[p])
            p+=1
        if waitlist:
            st,rt,jobnum=heapq.heappop(waitlist)
            cnt+=1
            time+=st #실수
            returntime[jobnum]=time-rt
        else:
            if p<n:
                time=joblist[p][1]
        
    answer = sum(returntime)//n
    return answer