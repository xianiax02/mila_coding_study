#서로소인 구간에서의 숫자개수--> 오일러 피
n=int(input())
temp=n
for num in range(2,int(n**(0.5))+1):
    if temp%num==0:
        n-=n//num
        while temp%num==0:
            temp//=num #한번 사용된 소인수를 끝까지 뺴줌.
if temp>1:
    n-=n//temp
print(n)
    