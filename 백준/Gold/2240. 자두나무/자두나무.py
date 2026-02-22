import sys
input=sys.stdin.readline
t,w=map(int,input().split())
seq=[0]
d=[[0]*(t+1) for _ in range(w+1)]
for _ in range(t):
    seq.append(int(input()))


for time in range(1,t+1):
    for n in range(0,w+1):
        if n!=0:
            if seq[time]-1==n%2:
                d[n][time]=max(d[n][time-1],d[n-1][time-1])+1
            else:
                d[n][time]=max(d[n][time-1],d[n-1][time-1])
        else:
            if seq[time]==1:
                d[n][time]=d[n][time-1]+1
            else:
                d[n][time]=d[n][time-1]

print(max([d[i][t] for i in range(w+1)]))