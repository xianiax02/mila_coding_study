#세그먼트 트리를 채우는 조건이 자식 노드 중 최솟값을 부모노드에 넣는 것이면 됨. 
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
height=1
inf=float('inf')
while pow(2,height)<n:
    height+=1

size=pow(2,height+1)-1 #실제 트리의 노드 갯수
tree=[inf]*(size+1) #배열의 크기는 0-padding

increment=pow(2,height) #인덱스와 주어진 배열 번호의 관계 1번 -> increment+1
for i in range(increment+1,increment+n+1):
    num=int(input())
    tree[i]=num
#세그먼트 트리 채우기. --> 최솟값으로
for index in range(size,0,-2): #거꾸로 가기. 
    tree[index//2]=min(tree[index],tree[index-1])
#범위 찾기 커맨드

for _ in range(m):
    a,b=map(int,input().split())
    result=[]
    start=a+increment
    end=b+increment
    ans=min(tree[start],tree[end])
    while start<=end: 
        if start%2 : #오른쪽 노드일때
            ans=min(tree[start],ans)
            start=(start+1)//2
        else:# 왼쪽노드일때
            start=start//2
        if end%2: #오른쪽 노드일때
            end=end//2
        else:
            ans=min(ans,tree[end])
            end=(end-1)//2 #다음으로 업데이트하는 거 잊음
    print(ans)
