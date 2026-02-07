def solution(m, n, puddles):
    MOD=1000000007
    inf=float("inf")
    d=[[0]*(m+1) for _ in range(n+1)]
    d[1][0]=1
    for (pj,pi) in puddles:
        d[pi][pj]=-1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if d[i][j]!=-1 and not (d[i-1][j]==d[i][j-1]==-1):
                if d[i-1][j]==-1:
                    d[i][j]=(d[i][j-1])%MOD
                elif d[i][j-1]==-1:
                    d[i][j]=(d[i-1][j])%MOD
                else:
                    d[i][j]=(d[i-1][j]+d[i][j-1])%MOD
                    
                
    
    print(d)        
    answer = d[n][m]
    return answer