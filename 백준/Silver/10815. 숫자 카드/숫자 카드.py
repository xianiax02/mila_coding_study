import sys
input=sys.stdin.readline
n=int(input())
cards=set(map(int,input().split()))
m=int(input())
answer=[]
checks=list(map(int,input().split()))
for check in checks:
    if check in cards:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)