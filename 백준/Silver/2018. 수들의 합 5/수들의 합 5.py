import sys
N=10**7
input=sys.stdin.readline
#numbers=[0]+[i for i in range(1,N+1)] #0부터 N까지의 배열, 인덱스 맞추기 위해 제로 패딩
a=int(input().strip())
p1=0
p2=1
cnt=1
s=1
while p2!=a:
    if s==a:
        cnt+=1
        p2+=1
        s+=p2 
    elif s<a:
        p2+=1
        s+=p2
    else:
        s-=p1
        p1+=1
sys.stdout.write(str(cnt)) 