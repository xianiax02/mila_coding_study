def findmaxearning(day,current_earning,table):
    if day>=len(table):
        return current_earning
    skipresult=findmaxearning(day+1,current_earning,table)
    takeresult=current_earning
    duration=table[day][0]
    earning=table[day][1]
    if day+duration<=len(table):
        takeresult=findmaxearning(day+duration, current_earning+earning, table)
    return max(skipresult,takeresult)

dday=int(input())
table=[]
for _ in range(dday):
    day=list(map(int,input().split()))
    table.append(day)

maxearning=findmaxearning(0,0,table)
print(maxearning)
