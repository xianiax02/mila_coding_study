import heapq
def solution(n, costs):
    answer = 0
    roads=[]
    parent=[i for i in range(n)]
    def find(a):
        if parent[a]==a:
            return a
        parent[a]=find(parent[a])
        return parent[a]
    def union(a,b):
        a=find(a)
        b=find(b)
        if a!=b:
            parent[max(a,b)]=min(a,b) 
    for cost in costs:
        a,b,w=cost
        heapq.heappush(roads,(w,a,b))
    while roads:
        w,a,b=heapq.heappop(roads)
        a=find(a)
        b=find(b)
        if a!=b:
            answer+=w
            union(a,b)
    return answer