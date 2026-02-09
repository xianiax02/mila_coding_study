def solution(progresses, speeds):
    def gauss(a):
        if a>int(a):
            return int(a+1)
        else:
            return int(a)
    answer = []
    n=len(progresses)
    r=[gauss((100-progresses[i])/speeds[i]) for i in range(n)]
    
    p1=0
    p2=0
    while p2<n:
        cnt=0
        while p2<n and r[p1]>=r[p2] :
            cnt+=1
            p2+=1
        p1=p2
        answer.append(cnt)
        
    return answer