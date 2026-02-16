import sys
input=sys.stdin.readline
n,k=map(int,input().split())
things=[]
for _ in range(n):
    things.append(list(map(int,input().split())))
    
d=dict()
d[0]=0
for (nw,nv) in things:
    new_d=dict()
    for w,v in d.items():
        new_d[w]=v
    for w,v in d.items():
        if w+nw<=k:
            new_d[w+nw]=max(d.get(w+nw,0),d.get(w,0)+nv)
    d=new_d

answer=max([i for i in d.values()])
print(answer)
