from queue import PriorityQueue
import sys
input=sys.stdin.readline
n=int(input().strip())
pq=PriorityQueue()
#data= (endtime,starttime)
for _ in range(n):
    starttime,endtime=map(int,input().split())
    pq.put((endtime,starttime))
cnt=0
oldend=0
while not pq.empty():
    newend,newstart=pq.get()
    if oldend<=newstart:
        cnt+=1
        oldend=newend


print(cnt)
