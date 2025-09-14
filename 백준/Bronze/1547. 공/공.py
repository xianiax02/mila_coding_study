
num=int(input())
cup=[1,2,3]

for _ in range(num):
    m,n=list(map(int,input().split(' ')))
    M=cup.index(m)
    N=cup.index(n)
    cup[M],cup[N]=cup[N],cup[M]

print(cup[0])