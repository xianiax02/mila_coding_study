import heapq
def solution(book_time):
    bt1=[]
    rooms=[]
    time=[0]*(60*24+10+1)
    answer=1
    convert=lambda x: 60*x[0]+x[1]
    for s,e in book_time:
        s,e=list(map(int,s.split(':'))),list(map(int,e.split(':')))
        bt1.append((convert(s),convert(e)+10))
    for s,e in bt1:
        time[s]+=1
        time[e]-=1
    maxroom=0
    val=0
    for t in time:
        val+=t
        maxroom=max(maxroom,val)
    

    return maxroom