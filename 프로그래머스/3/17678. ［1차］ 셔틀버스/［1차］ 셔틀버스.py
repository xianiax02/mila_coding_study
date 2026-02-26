def solution(n, t, m, timetable):
    convert= lambda x : int(x[:2])*60+int(x[3:])
    timetable=[convert(time) for time in timetable]
    timetable.sort()
    bustime,buscnt,pos=9*60,1,0
    print(timetable)
    while buscnt<=n:
        inthisbus=0
        while inthisbus<m and pos<len(timetable) and timetable[pos]<=bustime:
            pos+=1
            inthisbus+=1
        if buscnt==n:
            if inthisbus<m: #마지막 차가 다 안찼다면, 아무도 안탄것 포함
                answer=bustime
            else:
                answer=timetable[pos-1]-1
        bustime+=t
        buscnt+=1
    answer = f'{answer//60:02d}:{answer%60:02d}'
    return answer