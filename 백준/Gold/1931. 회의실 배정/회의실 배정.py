import sys
input=sys.stdin.readline
n=int(input())
meetings=[]
for _ in range(n):
    meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x: (x[1],x[0]))  #종료시간으로 정렬하기
count=0
time=0
for meeting in meetings:
    start,end=meeting
    if start>=time:
        count+=1
        time=end #완료시점으로 넘어감.


print(count)