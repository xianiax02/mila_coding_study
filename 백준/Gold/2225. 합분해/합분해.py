n,k=map(int,input().split())
mod=1000000000
dp=dict()
for i in range(n+1):
    dp[i]=1
for _ in range(k-1):
    new_dp=dict()
    for i,v in dp.items():
        for num in range(n+1):
            if i+num<=n:
                new_dp[i+num]=(new_dp.get(i+num,0)+v)%mod
    dp=new_dp

print(dp[n])