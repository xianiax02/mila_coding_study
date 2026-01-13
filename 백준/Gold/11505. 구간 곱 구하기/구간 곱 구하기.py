#수의 변경이 빈번히 일어남. 그리고 구간 곱을 구해야함 -> 세그먼트 트리
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())

height=0
while pow(2,height)<n:
    height+=1

size=pow(2,height+1)-1
offset=pow(2,height) # number+offset=arrayindex
tree=[1]*(size+1) #0-padding

for i in range(1,n+1):
    tree[i+offset]=int(input())

#build segment tree
for i in range(size,0,-2):
    tree[i//2]=(tree[i]*tree[i-1])%1000000007
    
for _ in range(m+k):
    command,a,b=map(int,input().split())
    if command==1:
        temp=tree[offset+a]
        #나눌떈 항상 zerodivision생각하기
        target=offset+a
        tree[target]=b%1000000007
        while target>0:            
            target=target//2
            tree[target]=(tree[2*target]*tree[2*target+1])%1000000007
            
    elif command==2:
        ans=1
        start=a+offset
        end=b+offset
        while start<=end:
            if start%2:
                ans=(ans*tree[start])%1000000007
                start+=1
            if not end%2:
                ans=(ans*tree[end])%1000000007
                end-=1
            start=start//2
            end=end//2
        print(ans)