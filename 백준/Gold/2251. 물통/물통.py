from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write
a,b,c=map(int,input().split())
capacity=[a,b,c]
ans=set()
records=set()
mq=deque()
currentstatus=[0,0,c]
records.add(tuple(currentstatus))
mq.append(currentstatus)
if not currentstatus[0]:
    ans.add(currentstatus[2])
while mq:
    currentstatus=mq.popleft()[:]
    #status에서 나올 수 있는 모든 분기를 다시 집어넣기, 대신 상태가 record에 적혀있는 것과 같으면 방문한거로 생각해서 제외
    for giver in range(3):
        for reciever in range(3):
            amount=min(currentstatus[giver],capacity[reciever]-currentstatus[reciever])
            #만약 기버가 못 주는 상황-> 기버가 0 이면 amount=0 조건 걸림
            #만약 리시버가 못 받는 상황-> 커파와 같음 amount=0 조건 걸림
            if amount>0 and giver!=reciever: #둘이 겹치는 상황 고려 못함. 점검 해줘야함.
                #update recievable and givable for currentstatus
                amount=min(currentstatus[giver],capacity[reciever]-currentstatus[reciever]) #전자->주는 물통이 빌때 후자-> 받는 물통이 다 찰떄
                nextstatus=currentstatus[:]
                nextstatus[giver]=currentstatus[giver]-amount
                nextstatus[reciever]=currentstatus[reciever]+amount
                if tuple(nextstatus) not in records:
                    mq.append(nextstatus)
                    records.add(tuple(nextstatus))#set은 add
for record in records: #set에는 리스트를 넣을 수 없으니 튜플로 바꿔서 record set에 넣기. set은 이진트리라 O(1)이니 사용
    if record[0]==0:
        ans.add(record[2])
for num in sorted(ans): #set은 정렬안되어있음 
    print(str(num)+' ')        