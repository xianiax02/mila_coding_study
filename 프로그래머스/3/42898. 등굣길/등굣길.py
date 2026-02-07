def solution(m, n, puddles):
    MOD=1000000007
    inf=float("inf")
    d=[[1]*(m+1) for _ in range(n+1)]
    for i in range(1,m+1):
        d[0][i]=0
    for i in range(1,n+1):
        d[i][0]=0
    d[1][0]=1
    for (pj,pi) in puddles:
        d[pi][pj]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if d[i][j]!=0:
                d[i][j]=(d[i-1][j]+d[i][j-1])%MOD
    
    print(d)        
    answer = d[n][m]
    return answer