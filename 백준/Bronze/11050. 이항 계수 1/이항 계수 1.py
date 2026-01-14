#이항계수의 점화식 -> C[n][k]=C[n-1][k]+C[n-1][k-1]
N,K=map(int,input().split())
C=[[0]*(N+1) for _ in range(N+1)]


for n in range(N+1):
    C[n][0]=1
    for k in range(1,n+1):
        C[n][k]=C[n-1][k]+C[n-1][k-1]

print(C[N][K])