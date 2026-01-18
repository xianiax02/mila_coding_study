t,l,r=map(int,input().split())
MOD=1000000007
DP=[[[0]*(1+r) for _ in range(1+l)] for _ in range(t+1)]
DP[1][1][1]=1

for i in range(2,t+1):
    for n in range(1,l+1):
        for m in range(1,r+1):
            DP[i][n][m]=(DP[i-1][n][m]*(i-2)+(DP[i-1][n-1][m])+(DP[i-1][n][m-1]))%MOD

print(DP[t][l][r]%MOD)