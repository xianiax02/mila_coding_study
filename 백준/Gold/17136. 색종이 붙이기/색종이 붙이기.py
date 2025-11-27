import sys
#input=sys.stdin.readline
paper=[]
answer=99999
amount=[0]+[0]*5 #1base indexing
for _ in range(10):
    paper.append(list(map(int,input().strip().split())))

def check(kernelsize,originrow,origincolumn): 
    global paper
    if originrow + kernelsize > 10 or origincolumn + kernelsize > 10:
        return False
    for i in range(kernelsize):
        for j in range(kernelsize):
            if paper[originrow+i][origincolumn+j]==0:
                return False
    return True

def elliminate(kernelsize,originrow,origincolumn): 
    global paper
    for i in range(kernelsize):
        for j in range(kernelsize):
            paper[originrow+i][origincolumn+j]=0

def restore(kernelsize,originrow,origincolumn): 
    global paper
    for i in range(kernelsize):
        for j in range(kernelsize):
            paper[originrow+i][origincolumn+j]=1

def paperfunc(posrow,poscol,cnt): #kernelsize를 5부터 1로 감소-
    global answer
    if poscol == 10: # 줄 바꿈
        posrow += 1
        poscol = 0
    if answer<cnt: #가지치기 최소갯수 아니면 취소
        return
    while posrow < 10 and paper[posrow][poscol] == 0:
        poscol += 1
        if poscol == 10: # 줄 바꿈
            posrow += 1
            poscol = 0
    if posrow>=10 : #끝까지 돌았을때
        answer=min(answer,cnt)
        return
#    for kernelsize in range(10,0,-1):
    for kernelsize in range(5,0,-1):
        if amount[kernelsize]==5: #5장 다 썼으면 다음 단계로 넘어가고, 아니면 같은 크기 더 탐색해보기
            continue
        if paper[posrow][poscol]: #and kernelsize+i-1<10 and kernelsize+j-1<10
            if check(kernelsize,posrow,poscol):
                elliminate(kernelsize,posrow,poscol)
                amount[kernelsize]+=1
                paperfunc(posrow,poscol+1,cnt+1)
                amount[kernelsize]-=1
                restore(kernelsize,posrow,poscol)



paperfunc(0,0,0)
if answer==99999:
    print(-1)
else:
    print(answer)
'''
sum=0
for i in range(10):
    for j in range(10):
        sum+=paper[i][j]
if not sum:
    print(0)
'''    