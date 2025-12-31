N=10000000
n=int(input())
numbers=[0]*(N+1)
for i in range(2,N+1):
    numbers[i]=i
for num in range(2,int(N**(1/2))+1):
    if numbers[num]:
        for mul in range(num+num,N,num):
            numbers[mul]=0

for num in range(2,N+1):
    if numbers[num]:
        target=str(numbers[num])
        startindex=0
        endindex=len(target)-1 #1 안빼는거 실수
        check=1
        while startindex<endindex :
            if target[startindex]!=target[endindex]:
                check=0
                break
            startindex+=1
            endindex-=1
        if not check:
            numbers[num]=0
find=0

while not find:
    if numbers[n]:
        print(n)
        find=1
    n+=1