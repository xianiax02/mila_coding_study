N,K=map(int,input().split())
C=[[0]*(1+N) for _ in range(1+N)]
MOD=10007
C[1][1]=1
C[1][0]=1
for n in range(2,N+1): #1부터 시작해도 0쪽은 상관이없으므로
    C[n][0]=1
    for k in range(1,n+1):
        C[n][k]=(C[n-1][k]+C[n-1][k-1])%MOD

print(C[N][K])