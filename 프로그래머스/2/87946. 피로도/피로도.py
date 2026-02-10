def solution(k, dungeons):
    n=len(dungeons)
    visited=[0]*(n)
    answer=-1
    count=0
    def dfs(x,ck):
        nonlocal count
        count=max(count,visited[x])
        for i in range(n):
            if not visited[i] and ck>=dungeons[i][0]:
                visited[i]=visited[x]+1
                dfs(i,ck-dungeons[i][1])
                visited[i]=0
    for i in range(n):
        if k>=dungeons[i][0]:
            visited[i]=1
            dfs(i,k-dungeons[i][1])
            visited[i]=0
    answer = count
    return answer