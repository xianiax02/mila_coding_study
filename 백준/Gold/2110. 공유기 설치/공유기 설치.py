#좌표 숫자가 범상치 않다--> 이진탐색
from bisect import bisect_left
import sys
input=sys.stdin.readline
n,c=map(int,input().split())
home=[]
for _ in range(n):
    home.append(int(input()))
home.sort()
def isok(d):
    cnt=0
    pos=0 #맨 처음 집부터 시작
    while pos<n:
        cnt+=1
        pos=bisect_left(home,home[pos]+d) #간격이 d 이상인 다음 위치를 찾는다
    if cnt<c:
        return False
    else:
        return True
    
start,end=1,home[-1]-home[0]
while start<=end:
    mid=(start+end)//2
    if isok(mid):
        start=mid+1
    else:
        end=mid-1
print(end)