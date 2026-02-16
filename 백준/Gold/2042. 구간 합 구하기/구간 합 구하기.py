import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())

s=1
while s<n:
    s<<=1

segtree=[0]*(2*s) #index: 1~2s-1
for i in range(s,s+n):
    segtree[i]=int(input())

for i in range(s-1,0,-1):
    segtree[i]=segtree[i<<1]+segtree[(i<<1)+1]
    
for _ in range(m+k):
    c,a,b=map(int,input().split())
    if c==1:
        a=s+a-1
        segtree[a]=b
        a>>=1
        while a>0:
            segtree[a]=segtree[a<<1]+segtree[(a<<1)+1]
            a>>=1
    
    elif c==2:
        a=s+a-1
        b=s+b-1
        ans=0
        while a<=b:
            if a%2==1:
                ans+=segtree[a]
                a+=1
            if b%2==0:
                ans+=segtree[b]
                b-=1
            a>>=1
            b>>=1
        print(ans)
                