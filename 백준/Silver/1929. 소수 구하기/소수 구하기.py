m,n=map(int,input().split())
isprime=[True]*(1+n)
isprime[0],isprime[1]=False,False
for num in range(2,int(n**(1/2))+1):
    if isprime[num]:
        for target in range(num*2,n+1,num):
            isprime[target]=False

for num in range(m,n+1):
    if isprime[num]:
        print(num)