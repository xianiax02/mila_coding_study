import sys
input=sys.stdin.readline
n=int(input())
answer=0
cards=list(map(int,input().split()))
cards=[0]+cards
dp=[0]*(n+1)
for i in range(n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+cards[j])

print(dp[n])