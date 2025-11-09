import sys
input=sys.stdin.readline
print=sys.stdout.write
num=list(map(int,input().strip()))
n=len(num)
for i in range(n):
    maxdigit=0
    for j in range(i,n):
        maxdigit=max(num[j],maxdigit)
        maxindex=num.index(maxdigit,i,n)
        num[i],num[maxindex]=num[maxindex],num[i]

ans=''.join(map(str,num))
print(str(ans))
    
