def solution(arr):
    n=len(arr)//2
    inf=float("inf")
    max_dp=[[0]*(n+1) for _ in range(n+1)]
    min_dp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        idx=2*i
        max_dp[i][i],min_dp[i][i]=map(int,[arr[idx],arr[idx]]) #자기 자신
    
    for d in range(1,n+1):
        for i in range(n+1-d):
            j=i+d
            maxval=-inf
            minval=inf
            for k in range(i,j):
                if arr[2*k+1]=='-':
                    maxval=max(maxval,(max_dp[i][k]-min_dp[k+1][j]))
                    minval=min(minval,(min_dp[i][k]-max_dp[k+1][j]))
                else:
                    maxval=max(maxval,(max_dp[i][k]+max_dp[k+1][j]))
                    minval=min(minval,(min_dp[i][k]+min_dp[k+1][j]))
            max_dp[i][j]=maxval
            min_dp[i][j]=minval
    answer = max_dp[0][n]
    return answer