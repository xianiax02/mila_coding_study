def gcd(a,b):
    if a<b:
        a,b=b,a
    #a > b
    while a%b !=0:
        temp=b
        b=a%b
        a=temp    
    return b

def lcm(a,b):
    g=gcd(a,b)
    am=a//g
    bm=b//g
    return am*bm*g

import sys
#input=sys.stdin.readline
n=int(input().strip())
for _ in range(n):
    a,b=map(int,input().split())
    print(lcm(a,b))