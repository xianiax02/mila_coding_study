import sys
input=sys.stdin.readline
n=int(input())
c=[0]*(n+1) #0-padding
for i in range(1,n+1):
    c[i]=list(map(int,input().split()))
dp=[0]*(n+2)
for i in range(n,0,-1):
    if i+c[i][0]-1>n: #enddate
        dp[i]=max(0,dp[i+1])
    else:
        dp[i]=max(dp[i+c[i][0]]+c[i][1],dp[i+1])
    
print(dp[1])