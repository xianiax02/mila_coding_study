import heapq
def solution(distance, rocks, n):
    rocks=[0]+rocks+[distance]
    rocks.sort()
    def determine(a,n):
        cnt=0
        prevlist=[0]
        for i in range(1,len(rocks)):
            prev=-prevlist[0]
            if rocks[i]-rocks[prev]<a:
                cnt+=1
                #원래는 삭제해야하나 애초에 넣지 않는다
                if cnt>n:
                    return False
            else: heapq.heappush(prevlist,-i)
        return True #indention 실수
    start,end=1,distance
    while start<=end:
        mid=(start+end)//2
        if determine(mid,n):
            start=mid+1
        else:
            end=mid-1
    answer=end
    return answer