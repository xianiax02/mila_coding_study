import sys
import heapq
input=sys.stdin.readline
n=int(input())
tasklist=[[] for _ in range(1+n)] #끝나는 날 기준으로 저장하기 위해 0-padding
maxval=[0]*(n+1)
for s in range(1,n+1):
    duration,w=map(int,input().split())
    e=s+duration-1
    if e<=n:
        tasklist[e].append((s,w))

for i in range(1,n+1):
    candidates=[]
    val=maxval[i-1] #오늘로 끝나는 사건을 고르지 않았을 때
    for task in tasklist[i]:
        val=max(val,task[1]+maxval[task[0]-1]) #i날에 끝나는 태스크를 고른것들에 대해서 가장 큰 값이 선정됨.
    maxval[i]=val

print(maxval[n])
    