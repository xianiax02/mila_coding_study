import sys
#input=sys.stdin.readlin
n=int(input())
#순열 배열을 만들어서 호출이 빠르게 일어나도록 하자
factorial=[1]*(1+n)
for i in range(1,1+n):
    factorial[i]=factorial[i-1]*i
command=list(map(int,input().split()))


if command[0]==1:
    result=[]
    numbers=list(range(1,n+1))
    k=command[-1]-1 #0-base indexing하니까 맞음.
    for i in range(n,0,-1):
        digit=i
        if k//factorial[digit-1]>=0:
            order=k//factorial[digit-1] #몇번째로 작아야하는가?
            result.append(numbers.pop(order))
            k=k%factorial[digit-1]
        else:
            result.append(numbers.pop(0)) #pop 하면 자동으로 숫자가 당겨짐. 

    print(*result)

elif command[0]==2:
    ans=1
    p=command[1:]
    belownum=[i-1 for i in range(n+1)] #인덱스 실수 할뻔. 인덱스-1
    #지금 주어진 순열의 최대 자릿수가 몇인가?
    for i,num in enumerate(p):
        digit=n-i
        ans+=belownum[num]*factorial[digit-1]
        for j in range(num,n+1):
            if belownum[j]!=0:
                belownum[j]-=1
    print(ans)
                 