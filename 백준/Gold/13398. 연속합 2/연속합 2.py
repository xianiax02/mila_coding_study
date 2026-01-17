import sys
input=sys.stdin.readline
n=int(input())
numlist=list(map(int,input().split()))
DL=[0]*(n) #i번째를 반드시 포함하는 i번째 까지의 부분합
DR=[0]*(n)
DL[0]=numlist[0]
DR[-1]=numlist[-1]
for i in range(1,n):
    DL[i]=max(numlist[i]+DL[i-1],numlist[i])
for i in range(n-2,-1,-1):    
    DR[i]=max(numlist[i]+DR[i+1],numlist[i])
ans=max(max(DL),max(DR))
ans=max(DR[0],ans,DL[n-1])
for i in range(1,n-1):
    ans=max(ans,DL[i-1]+DR[i+1])

print(ans)