def solution(temperature, t1, t2, a, b, onboard):
    inf=float('inf')
    for i,state in enumerate(onboard):
        if state==1:
            start=i
            break
    n=len(onboard)
    for i in range(n-1,-1,-1):
        if onboard[i]==1:
            end=i
            break
    duration=end-start
    d=dict()
    print(start,end,duration)
    #dp 초기 상태 설정 -> starttime 에서의 d 상태 
    for t in range(t1,t2+1):
        if temperature>=t2 and temperature-t<=start:
            d[t]=(temperature-t)*a #t까지 내려오는데 걸리는 시간
        elif temperature<=t1 and t-temperature<=start:
            d[t]=(t-temperature)*a
    for step in range(duration):
        new_d=dict()
        for (temp,cost) in d.items():
            if (temp<t1 or temp>t2) and onboard[start+step]: #탑승자가 있는데, 온도 범위가 벗어났으면
                continue #new_d에 넣지 않고 건너뛴다. 
            if temperature>t2:
                new_d[temp-1]=min(d[temp]+a,new_d.get(temp-1,inf))
                new_d[temp+1]=min(d[temp],new_d.get(temp+1,inf))
            elif temperature<t1:
                new_d[temp+1]=min(d[temp]+a,new_d.get(temp+1,inf))
                new_d[temp-1]=min(d[temp],new_d.get(temp-1,inf))
            if temp!=temperature:
                new_d[temp]=min(d[temp]+b,new_d.get(temp,inf))
            else:
                new_d[temp]=min(d[temp],new_d.get(temp,inf))
        d=new_d       
                
    answer = min([val for temp,val in d.items() if (temp<=t2 and temp>=t1)])
    return answer