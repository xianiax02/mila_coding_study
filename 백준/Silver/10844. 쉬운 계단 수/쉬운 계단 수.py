n=int(input())
f1=[0,1,1,1,1,1,1,1,1,1]
MOD=10**9
if n>=2:
    for i in range(2,n+1): #f2~fn
        f2=[0]*10
        for num in range(1,9): 
            f2[num]=(f1[num-1]+f1[num+1])%MOD #양끝에서 오므로
        f2[0]=f1[1]
        f2[9]=f1[8]
        
        f1=f2[:] #깊은 복사 
    print(sum(f1)%MOD)
else:
    if n==1:
        print(sum(f1))