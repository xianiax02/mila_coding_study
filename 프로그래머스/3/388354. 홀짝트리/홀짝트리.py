import sys
sys.setrecursionlimit(10**6)
def solution(nodes, edges):
    treelist=[]
    def dfs(v,l):
        for nxt in adlist[v]:
            if not visited[nxt]:
                visited[nxt]=True
                l.append(nxt)
                dfs(nxt,l)
    hnum=0 #type 0
    rnum=0 #type 1
    typelist=[0 for _ in range(max(nodes)+1)]
    visited=[False]*(max(nodes)+1)
    #make adlist
    adlist=[[] for _ in range(max(nodes)+1)]
    for edge in edges:
        a,b=edge
        adlist[a].append(b)
        adlist[b].append(a)
    for node in nodes:
        if node%2!=len(adlist[node])%2:
            typelist[node]=1
        if not visited[node]:
            treelist.append([node])
            visited[node]=True
            dfs(node,treelist[-1])
    for tree in treelist:
        treetypes=[]
        for node in tree:
            treetypes.append(typelist[node])
        if treetypes.count(0)==1:
            hnum+=1
        if treetypes.count(1)==1:
            rnum+=1
    answer = [hnum,rnum]
    return answer