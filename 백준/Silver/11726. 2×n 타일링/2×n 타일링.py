n=int(input())
f0,f1,f2=0,1,2
MOD=10007
if n>=3:
    for _ in range(3,n+1): #루프한번에 f가 하나 생기므로 f3~fn 까지 반복 돌려야함.
        f3=(f1+f2)%MOD #==f[n]=2f[n-2]+f[n-1]
        f1,f2=f2,f3
    print(f2)
else:
    print(n)


        
