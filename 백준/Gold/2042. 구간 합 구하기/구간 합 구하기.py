import sys
input=sys.stdin.readline
print=sys.stdout.write
n,m,k=map(int,input().split())
#이진트리이므로 leafnode에 n개 숫자를 모두 담을 수 있는 리프 크기를 구한다. 
S=1
while S<n:
    S<<=1
segtree=[0]*(2*S) #리프 노드 크기는 S 트리는 1~S
#입력하기
for i in range(S,S+n):
    segtree[i]=int(input().strip())
#채워넣기
for i in range(S-1,0,-1):
    segtree[i]=segtree[(i<<1)+1]+segtree[i<<1]
    
for _ in range(m+k):
    command,a,b=map(int,input().split())
    if command==1: #숫자 변경
        idx=S+a-1
        segtree[idx]=b
        idx>>=1
        while idx>0:
            segtree[idx]=segtree[2*idx+1]+segtree[2*idx]
            idx>>=1

    elif command==2: #조회
        ans=0
        a=S+a-1
        b=S+b-1
        while a<=b:
            if a%2==1: # a가 오른쪽 자식이면
                ans+=segtree[a]
                a+= 1
            if b%2==0: # b가 왼쪽 자식이면
                ans+=segtree[b]
                b-=1
            a>>=1
            b>>=1
        print(str(ans)+'\n')
        
        