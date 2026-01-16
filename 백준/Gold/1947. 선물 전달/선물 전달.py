MOD=10**9
n=int(input())
function=[0]*(1+n)
function[0]=1
function[1]=0
for i in range(2,1+n):
    function[i]=((i-1)*(function[i-1]+function[i-2]))%MOD

print(function[n])