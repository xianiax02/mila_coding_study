n=int(input().strip())
m=int(input().strip())
#make parent array
parent=[i for i in range(n)]
def find(x):
    global parent
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    global parent
    a=find(a)
    b=find(b)
    if a!=b:
        parent[a]=min(a,b)
        parent[b]=min(b,a)
    
#실제는 1부터 시작이지만 0부터 시작인걸로 간주-> 이후 여행 계획 입력 받을때 -1해서 비교
for currentnode in range(n): #윗대각행렬 성분에 대해서만 UNION 적용
    command=list(map(int,input().split()))
    for subjectnode in range(currentnode,n):
        if command[subjectnode]==1:
            union(currentnode,subjectnode)

plan=list(map(int,input().split()))
find(plan[0]-1)
root=parent[plan[0]-1]
possible=True

for checkpoint in plan:
    find(checkpoint-1)
    if parent[checkpoint-1]!=root: #다른 집합에 소속될때
        possible=False
        print('NO')
        break
    root=parent[checkpoint-1]
    
if possible:
    print('YES')