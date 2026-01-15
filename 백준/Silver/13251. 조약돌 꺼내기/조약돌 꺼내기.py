#조합 테이블 만들고 호출해서 하자 어차피 M도 50 이하
import sys
input=sys.stdin.readline
N=50**2
C=[[0]*(1+N) for _ in range(1+N)]
C[1][0]=1
C[1][1]=1
for i in range(2,N+1):
    C[i][0]=1
    for j in range(1,i+1): # 실수로 똑같이 2로 설정함. 
        C[i][j]=C[i-1][j]+C[i-1][j-1]

m=int(input())
stonenum=list(map(int,input().split()))
k=int(input())
numerator=0
totalnum=sum(stonenum)
for i in range(m):
    if stonenum[i]>=k:
        numerator+=C[stonenum[i]][k]
denominator=C[totalnum][k]

ans=numerator/denominator
print(ans)