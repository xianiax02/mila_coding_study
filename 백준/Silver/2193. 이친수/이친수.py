n=int(input())
f=[0]*(n+1)
f[1]=1
if n>1:
    f[2]=1
for i in range(3,n+1):
    f[i]=2*f[i-2]+f[i-3]

print(f[n])