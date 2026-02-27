n=int(input())
dp=[1]*10
mod=10007
for _ in range(n-1):
    new_dp=[0]*10
    for i in range(10):
        for j in range(0,i+1):
            new_dp[i]+=dp[j]
        new_dp[i]%=mod
    dp=new_dp
print(sum(dp)%mod)