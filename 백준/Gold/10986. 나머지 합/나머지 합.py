import sys
input=sys.stdin.readline
n,m=map(int,input().strip().split())
numbers=[0]+[int(x) for x in input().strip().split()]
r=[0 for _ in range(n+1)]
cnt=0
remains=[0 for _ in range(m)]
for i in range(1,n+1):
    r[i]=((r[i-1]%m)+(numbers[i]%m))%m
    remains[r[i]]+=1
remains[0]+=1
for remainnum in remains:
    if remainnum>1:
        cnt+=remainnum*(remainnum-1)//2


sys.stdout.write(str(cnt))
