import sys
input=sys.stdin.readline
command=list(map(int,input().split()))
del command[-1] #마지막 0은 삭제
n=len(command)
def getw(start,end):
    if start==0:
        return 2
    elif start==end:
        return 1
    elif abs(start-end)==2:
        return 4
    else:
        return 3

dp={(0,0):0}
for target in command:
    new_dp={}
    for (l,r),w in dp.items():
        if target!=r: #왼쪽 움직일때
            if (target,r) in new_dp:
                new_dp[(target,r)]=min(new_dp[(target,r)],w+getw(l,target))
            else:
                new_dp[(target,r)]=w+getw(l,target)
        if target!=l: #오른쪽 움직일때
            if (l,target) in new_dp:
                new_dp[(l,target)]=min(new_dp[(l,target)],w+getw(r,target))
            else:
                new_dp[(l,target)]=w+getw(r,target)
        
    dp=new_dp

print(min(dp.values()))