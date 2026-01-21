import sys
n=int(input())
input=sys.stdin.readline
w=[] #0-padding
D=[[0 for j in range(1<<16)] for i in range(16) ]
for _ in range(n):
    weights=list(map(int,input().split()))
    w.append(weights)

def tsp(c,v):
    if v==(1<<n)-1:
        if w[c][0]==0:
            return float("inf")
        else:
            return w[c][0]
    if D[c][v]!=0:
        return D[c][v]
    min_val=float("inf")
    for i in range(0,n):
        if (v&(1<<i))==0 and w[c][i]!=0:
            min_val=min(min_val,tsp(i,v|(1<<i))+w[c][i])
    D[c][v]=min_val
    return D[c][v]
    
print(tsp(0,1))