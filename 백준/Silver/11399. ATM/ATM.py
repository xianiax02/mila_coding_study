import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
numbers=list(map(int,input().strip().split()))
for i in range(1,n):
    key=numbers[i]
    j=i-1
    while j>=0 and numbers[j]>key:
        numbers[j+1]=numbers[j]
        j-=1
    numbers[j+1]=key
ans=0
for index,num in enumerate(numbers):
    ans+=num*(n-index)

print(str(ans))