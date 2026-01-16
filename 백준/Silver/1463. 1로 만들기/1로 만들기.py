n=int(input())
inf=float("inf")
f=[inf]*(1+n)
f[1]=0
'''
for i in range(1,n+1):
    if 3*i<=n:
        f[3*i]=min(f[i]+1,f[3*i])
    if 2*i<=n:
        f[2*i]=min(f[i]+1,f[2*i])
    if i+1<=n:
        f[i+1]=min(f[i]+1,f[i+1])
print(f[n])
'''
for i in range(2,n+1):
    f[i]=f[i-1]+1
    if not i%2:
        f[i]=min(f[i//2]+1,f[i])
    if not i%3:
        f[i]=min(f[i//3]+1,f[i])
print(f[n])