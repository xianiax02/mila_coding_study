import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    dp={1:1,2:1,3:1}
    while len(dp)!=1:
        new_dp=dict()
        new_dp[n]=dp.get(n,0) #n은 보존
        for k,v in dp.items():
            for nxt in range(1,4):
                if k+nxt<=n:
                    new_dp[k+nxt]=new_dp.get(k+nxt,0)+v
        dp=new_dp
    print(dp[n])