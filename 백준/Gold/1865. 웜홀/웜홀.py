import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m,w=map(int,input().split())
    ncycle='NO'
    edgelist=[]
    distance=[0]*(n+1)
    for _ in range(m):
        a,b,ew=map(int,input().split())
        edgelist.append((ew,a,b))
        edgelist.append((ew,b,a))
    for _ in range(w):
        a,b,ew=map(int,input().split())
        edgelist.append((-ew,a,b))
    for turn in range(n):
        for ew,a,b in edgelist:
            if distance[a]+ew<distance[b]:
                distance[b]=distance[a]+ew
                if turn==n-1:
                    ncycle='YES'
    print(ncycle)