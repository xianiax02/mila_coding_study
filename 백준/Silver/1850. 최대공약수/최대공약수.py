def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
for _ in range(gcd(a,b)):
    print(1,end='')