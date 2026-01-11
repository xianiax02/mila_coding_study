import sys
import heapq
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
edges=[]
rootgraph=[i for i in range(n)]
totallength=0
result=[]
def find(x):
    if rootgraph[x]==x:
        return x
    rootgraph[x]=find(rootgraph[x])
    return rootgraph[x]

def union(a,b):
    roota=find(a)
    rootb=find(b)
    if roota!=rootb:
        rootgraph[max(roota,rootb)]=min(roota,rootb)
        
def tonum(char):
    if char.upper()==char:
        return ord(char)-38
    else:
        return ord(char)-96
#주어진 그래프를 엣지로 변환해서     
for com1 in range(n):
    command=input()
    for com2 in range(n):
        if command[com2]=='0':
            continue
        else:
            w=tonum(command[com2])
            totallength+=w
            heapq.heappush(edges,(w,com1,com2)) #방향은 상관없으니 거꾸로 할 필요없음. 어차피 union 하는 거라
cnt=0
while edges and cnt<n:
    currentedge=heapq.heappop(edges)
    w,s,e=currentedge
    roots=find(s)
    roote=find(e)
    if roots!=roote:
        union(s,e)
        result.append(currentedge)
        cnt+=1

if len(result)!=n-1:
    print(-1)
else:
    mstsum=0
    for edge in result:
        mstsum+=edge[0]
    ans=totallength-mstsum
    print(ans)