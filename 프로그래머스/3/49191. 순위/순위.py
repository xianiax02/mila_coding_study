import sys
sys.setrecursionlimit(10**6)
def solution(n, results):
    parent=[[] for _ in range(n+1)]
    child=[[] for _ in range(n+1)]
    dp=[None] *(n+1)
    dc=[None] *(n+1)
    answer = 0
    for result in results:
        winner,loser=result
        parent[loser].append(winner)
        child[winner].append(loser)
    def rollup(a,arr,d): #a 아래에 있는 사람들의 수 
        mem=set()
        if d[a] is not None:
            return d[a]
        for nxt in arr[a]:
            mem.add(nxt)  #nxt자기자신 포함
            mem|=rollup(nxt,arr,d)
        d[a]=mem
        return mem
    for i in range(1,n+1):
        rollup(i,parent,dp)
        rollup(i,child,dc)
        if len(dp[i])+len(dc[i])==n-1:
            answer+=1
    print(dp)
    print(dc)
    return answer