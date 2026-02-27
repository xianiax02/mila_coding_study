n=int(input())
dp=[1]*(n+1)
dp[1]=3
mod=9901
for i in range(2,n+1):
    dp[i]=(2*dp[i-1]+dp[i-2])%mod

print(dp[n])