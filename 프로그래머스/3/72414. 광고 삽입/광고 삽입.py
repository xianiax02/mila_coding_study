
def solution(play_time, adv_time, logs):
    starts=dict()
    ends=dict()
    for i,log in enumerate(logs):
        start,end=log.split('-')
        h,m,s=map(int,start.split(':'))
        start=3600*h+60*m+s
        h,m,s=map(int,end.split(':'))
        end=3600*h+60*m+s
        logs[i]=[start,end]
        starts[start]=starts.get(start,0)+1
        ends[end]=ends.get(end,0)+1
    h,m,s=map(int,play_time.split(':'))
    play_time=3600*h+60*m+s
    h,m,s=map(int,adv_time.split(':'))
    adv_time=3600*h+60*m+s
    n=play_time-adv_time
    cumuls=[0]*(n+1)
    plays=[0]*(play_time+1)
    for i in range(0,play_time+1):
        if i==0:
            plays[i]=starts.get(i,0)
        else:
            plays[i]=plays[i-1]+starts.get(i,0)-ends.get(i,0)
    firstcount=0
    for p in range(adv_time):
        firstcount+=plays[p]
    cumul=firstcount
    p1=0
    p2=p1+adv_time
    maxval,maxstart=firstcount,0
    for p1 in range(1,n+1):
        p2=p1+adv_time-1
        cumul=cumul-plays[p1-1]+plays[p2]
        if cumul>maxval:
            maxval=cumul
            maxstart=p1  
    h,m,s=[maxstart//3600,(maxstart%3600)//60,maxstart%60]    
    answer =f"{h:02d}:{m:02d}:{s:02d}"
    return answer