import sys 
input=sys.stdin.readline
n,qn=map(int,input().strip().split())
numbers=[[0 for _ in range(n+1)]]+[[0] for _ in range(n)]
for i in range(1,n+1):
    numbers[i]+=list(map(int,input().strip().split()))
s=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):        
        s[i][j]=s[i-1][j]+s[i][j-1]+numbers[i][j]-s[i-1][j-1]

for _ in range(qn):
    a,b,c,d=map(int,input().strip().split())
    answer=s[c][d]-s[a-1][d]-s[c][b-1]+s[a-1][b-1]
    sys.stdout.write(str(answer)+'\n')
