import heapq
def solution(book_time):
    bt1=[]
    rooms=[]
    answer=1
    convert=lambda x: 60*x[0]+x[1]
    for s,e in book_time:
        s,e=list(map(int,s.split(':'))),list(map(int,e.split(':')))
        bt1.append((convert(s),convert(e)+10))
    bt1.sort(key=lambda x: x[0])
    
    for s,e in bt1:
        if not rooms:
            heapq.heappush(rooms,e)
            continue
        if rooms[0]>s: #가장 빠르게 끝나는 숙박시간보다 일찍 들어가야하는 경우
            heapq.heappush(rooms,e)
            answer+=1
        else: #가장 빠르게 끝나는 숙박시간이 퇴실했을 경우
            heapq.heappop(rooms)
            heapq.heappush(rooms,e)
            rooms.sort()   
    return answer