import sys
sys.setrecursionlimit(10**6)
def solution(tickets):
    tickets.sort(key=lambda x:x[1]) #adlist에 추가할떄 가끔적이면 도착지점이 알파벳 빠른순으로 정렬됨
    #나중에 adlist[v].sort(key=lambda x:tickets[x][1])로 해도 되긴함. 
    startpoints=[]
    n=len(tickets)
    adlist=[[] for _ in range(n)]
    sdict=dict()
    visited=[False]*n
    for i,ticket in enumerate(tickets):
        s,e=ticket
        if s=='ICN':
            startpoints.append(i)
        l=sdict.get(s,[])
        l+=[i]
        sdict[s]=l
    for i, ticket in enumerate(tickets):
        s,e=ticket
        adlist[i]+=sdict.get(e,[])
    def dfs(v):
    # 1. 종료 조건 (정답을 찾았나?)
        if False not in visited:
            return True
    # 2. 다음 선택지 탐색
        for nxt in adlist[v]:
            if not visited[nxt]:
                answer.append(nxt)# [SAVE]
                visited[nxt]=True
                if dfs(nxt):              # [GO] 다음 단계로 전진!
                    return True                # 성공했다면 위로 쭉쭉 '성공' 전달
                visited[nxt]=False
                answer.pop()# [LOAD] 여기가 안 되면 돌아와서 복구
        return False # 여기까지 왔는데 성공 못 했으면 이 길은 '꽝'
    for start in startpoints:
        answer=[start]
        visited[start]=True
        if dfs(start):
            break
        visited[start]=False
    temp=[tickets[answer[0]][0]]
    for a in answer:
        temp.append(tickets[a][1])
    answer=temp
    return answer