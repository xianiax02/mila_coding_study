def solution(n, money):
    MOD=1000000007
    m=len(money)
    money.sort()
    d=[[0]*(n+1) for _ in range(m)]
    for j in range(n+1):
        if j%money[0]==0:
            d[0][j]+=1 #제일 작은 코인을 활용해 만들 수 있는 경우의 수
    for i in range(1,m):
        coin=money[i]
        for j in range(n+1):
            d[i][j]=(d[i-1][j]+d[i][j-coin])%MOD
    answer = d[m-1][n]
    return answer