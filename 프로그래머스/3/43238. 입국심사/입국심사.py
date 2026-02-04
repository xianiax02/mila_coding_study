def solution(n, times):
    def check(t,n):
        maxnum=0
        for workers in times:
            maxnum+=t//workers
        if n<=maxnum:
            return True
        else:
            return False
    start=min(times)
    end=min(times)*n
    while start<=end:
        mid=(start+end)//2
        if check(mid,n):
            end=mid-1
        else:
            start=mid+1
    answer=start
    return answer