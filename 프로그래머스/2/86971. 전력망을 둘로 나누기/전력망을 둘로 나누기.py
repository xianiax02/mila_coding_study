import sys
sys.setrecursionlimit(10**6)
def solution(n, wires):
    answer = float('inf')
    adlist=[[] for _ in range(n+1)]
    for wire in wires:
        a,b=wire
        adlist[a].append(b)
        adlist[b].append(a)
    def dfs(v,cnt):
        for nxt in adlist[v]:
            if not visited[nxt]:
                cnt[0]+=1
                visited[nxt]=True
                dfs(nxt,cnt)
    for wire in wires:
        visited=[False]*(1+n)
        s1,s2=wire
        adlist[s1].remove(s2)
        adlist[s2].remove(s1)
        cnt1=[0]
        cnt2=[0]
        visited[s1]=True
        visited[s2]=True
        dfs(s1,cnt1)
        dfs(s2,cnt2)
        answer=min(answer,abs(cnt1[0]-cnt2[0]))
        adlist[s1].append(s2)
        adlist[s2].append(s1)   
    return answer