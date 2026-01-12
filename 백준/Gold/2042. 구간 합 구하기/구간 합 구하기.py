import sys
input=sys.stdin.readline
leafn,m,k=map(int,input().split())
treedepth=0 #leafn 이 1부터 주어짐
while 2**treedepth<leafn:
    treedepth+=1

size=2**(treedepth+1)-1
increment=2**treedepth-1 #index+increment=treeindex
#전체 배열 크기 구하기
tree=[0]*(size+1) #0은 부분합 구하든 뭘하든 영향이 없으니 
for i in range(1,leafn+1):
    a=int(input())
    tree[i+increment]=a
#세그먼트 트리 채우기    
for i in range(size,0,-2):
    tree[(i-1)//2]=tree[i]+tree[i-1]
    
for _ in range(m+k):
    command,start,end=map(int,input().split())
    if command==1:
        diff=end-tree[start+increment]
        tree[start+increment]=end
        index=start+increment
        while index>=1:
            index=index//2 #go to parent
            tree[index]+=diff        
    elif command==2:
        selected={}
        ans=0
        start+=increment
        end+=increment
        while start<=end:#둘이 모이는 그 지점도 더해야함. 어차피 둘이 같을때 start==end 나머지는 0또는 1이니 둘중 하나에서만 더해지고 루프 끝남
            if start%2==1 :#시작이 오른쪽 노드일때
                ans+=tree[start]
                start=(start+1)//2
            else:
                start=(start)//2
            if end%2==0 : #끝이 왼쪽 노드일때
                ans+=tree[end]
                end=(end-1)//2
            else:
                end=(end//2)
        print(ans)
                