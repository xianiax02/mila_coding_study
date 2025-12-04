import sys
input=sys.stdin.readline
n,k=map(int,input().strip().split())
#동전의 가치가 서로 배수라서 그리디를 쓸 수 있다. 큰걸 썼다는 것은 백프로 작은걸 여러개 쓴 것과 같으니까 
coins=[]
for _ in range(n):
    coins.append(int(input().strip()))

cnt=0
amount=k
index=n-1
while amount!=0:
    num=amount//(coins[index])
    cnt+=num
    amount-=num*(coins[index])
    index-=1
        
print(cnt)   