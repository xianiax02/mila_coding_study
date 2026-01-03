n=int(input())
numerator=[0]*n
denominator=[0]*n
graph=[[0]*n for _ in range(n)] #사실삳 visited의 역할.
for _ in range(n-1):
    a,b,p,q=map(int,input().split())
    graph[a][b]=p
    graph[b][a]=q

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    g=gcd(a,b)
    return a*b//g
numerator[0]=1
denominator[0]=1         
for _ in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] :
                p=graph[a][b]
                q=graph[b][a] #같은 a에서 시작하므로 검출된다면 반드시 a라는 연결고리 존재
                #둘다 처음 작업하는 재료일때:
                if numerator[a]!=0 and numerator[b]==0: #a알고 b 알때만 방향성 있게 체크
                    denominator[b]=denominator[a]*p
                    numerator[b]=numerator[a]*q
                  
            #반드시 한쪽은 이미 작업한 재료. 이미 관계가 있는 재료일때
#기약분수 만들기
for i in range(n):
    l=gcd(numerator[i],denominator[i])
    numerator[i]=numerator[i]//l
    denominator[i]=denominator[i]//l

#분모의 최소공배수 구하기
m=lcm(denominator[0],denominator[1])
for i in range(2,n):
    m=lcm(m,denominator[i])

for i in range(n):
    c=m//denominator[i]
    numerator[i]*=c

d=gcd(numerator[0],numerator[1])
for i in range(2,n):
    d=gcd(d,numerator[i])

for num in numerator:
    print(num//d,end=' ')


