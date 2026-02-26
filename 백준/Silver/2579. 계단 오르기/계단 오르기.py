import sys
input=sys.stdin.readline
n=int(input())
scores=[0]
for _ in range(n):
    scores.append(int(input()))

dp=[0]*(n+1)
if n>=1:
    dp[1]=scores[1]
if n>=2:
    dp[2]=scores[1]+scores[2]
if n>=3:
    dp[3]=max(scores[1]+scores[3],scores[2]+scores[3])
if n>=4:
    for i in range(4,n+1):
        dp[i]=max(dp[i-2]+scores[i],scores[i]+scores[i-1]+dp[i-3])

print(dp[n])