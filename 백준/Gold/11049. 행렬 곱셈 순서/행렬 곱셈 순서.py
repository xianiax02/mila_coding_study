import sys
input=sys.stdin.readline
n=int(input())
arraysize=[(0,0) for _ in range(1+n)] #0-padding (0,0)*3--> 튜플이나 리스트 이렇게 하면 연장만 된다.
for i in range(1,n+1):
    r,c=map(int,input().split())
    arraysize[i]=(r,c)

D=[[0]*(n+1) for _ in range(n+1)] #시작은 1~n-1 끝은 1~n 아ㅏㄴ전하게 n+1로 선언
for interval in range(1,n): #구간이 짧은거에서 구간이 긴 값을 도출하므로 구간이 짧은 것들이 먼저 구해진다는 전제가 있어야함. 
    for start in range(1,n-interval+1):
        end=start+interval
        D[start][end]=float("inf")
        for k in range(start,end): #a부터 b까지면 케이스는 총 b-a개
            D[start][end]=min(D[start][k]+D[k+1][end]+arraysize[start][0]*arraysize[k][1]*arraysize[end][1],D[start][end])

print(D[1][n])