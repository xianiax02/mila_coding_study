from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write
a,b,c=map(int,input().split())
capacity=[a,b,c]
recievable=[0]*3
givable=[0]*3
ans=set()
records=[]
mq=deque()
currentstatus=[0,0,c]
records.append(currentstatus)
mq.append(currentstatus)
if not currentstatus[0]:
    ans.add(currentstatus[2])
while mq:
    currentstatus=mq.popleft()[:]
    #status에서 나올 수 있는 모든 분기를 다시 집어넣기, 대신 상태가 record에 적혀있는 것과 같으면 방문한거로 생각해서 제외
    for i in range(3):
        if currentstatus[i]==capacity[i]:
            givable[i]=1
            recievable[i]=0
        elif currentstatus[i]==0:
            givable[i]=0
            recievable[i]=1
        else:
            givable[i]=1
            recievable[i]=1
    for giver in range(3):
        for reciever in range(3):
            if givable[giver] and recievable[reciever] and giver!=reciever:
                #update recievable and givable for currentstatus
                amount=min(currentstatus[giver],capacity[reciever]-currentstatus[reciever]) #전자->주는 물통이 빌때 후자-> 받는 물통이 다 찰떄
                nextstatus=currentstatus[:]
                nextstatus[giver]=currentstatus[giver]-amount
                nextstatus[reciever]=currentstatus[reciever]+amount
                if nextstatus not in records:
                    mq.append(nextstatus)
                    records.append(nextstatus)
for i in range(len(records)):
    if records[i][0]==0:
        ans.add(records[i][2])
for num in sorted(ans):
    print(str(num)+' ')              
                