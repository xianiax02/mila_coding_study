import sys
#input=sys.stdin.readline
n=int(input().strip())
numbers=sorted(list(map(int,input().strip().split())))

def check(numbers,numindex,n):
    p1,p2=0,n-1
    while p1<p2:
        s=numbers[p1]+numbers[p2]
        if p1==numindex:
            p1+=1
            continue
        elif p2==numindex:
            p2-=1
            continue
        if s>numbers[numindex]:
            p2-=1
        elif s<numbers[numindex]:
            p1+=1
        else:
            return 1
    return 0

cnt=0
for i in range(n):
    if check(numbers,i,n):
        cnt+=1

sys.stdout.write(str(cnt))