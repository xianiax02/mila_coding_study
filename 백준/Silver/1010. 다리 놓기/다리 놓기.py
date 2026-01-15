#다리끼리는 서로 겹쳐질 수 없음. -> 좌변 우변으로 나누었을때, 좌변에서 이제 이어져야할 다리는 좌변의 전 다리의 도착점 이후의 우변이어야함.
#L[n]>L[n-1] or R[n]>R[n-1L] L[0]=n 서쪽 사이트기준이므로 L[n]>L[n-1]을 적용하면 됨. 모든 다리를 적용하기 위해서
#우측의 모든 사이트들 수-N(남은다리(N-n)들을 보장해야함.>L[n]>L[n-1]
#순서가 정해져있으니 각 쌍 내에서의 순서는 중요하지 않음--> 조합
#동쪽의 다리들에서 서쪽의 다리 갯수를 고르는 것 eCw=e-1Cw+e-1Cw-1
#e==w 일때 1, B[e][w]=B[e][w-1]+B[e]B[w]
#시간제한이 빡빡하고 사이트갯수가 30이하이니 DP행렬을 선언해서 접근
import sys
input=sys.stdin.readline
print=sys.stdout.write
N=30
B=[[0]*N for _ in range(N)]
B[1][0]=1
B[1][1]=1
for e in range(2,N):
    B[e][0]=1
    for w in range(1,e+1):
       B[e][w]=B[e-1][w]+B[e-1][w-1]
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())    
    print(str(B[m][n])+'\n')

    