import sys
input=sys.stdin.readline
n=int(input().strip())
goal=int(input().strip())
ans=0
materials=list(map(int,input().strip().split()))
materials.sort()
p1=0
p2=n-1
cnt=0
while p1<p2:
    s=materials[p1]+materials[p2]
    if s==goal:
        cnt+=1
        p1+=1
        p2-=1
    elif s>goal:
        p2-=1
    elif s<goal:
        p1+=1

sys.stdout.write(str(cnt))