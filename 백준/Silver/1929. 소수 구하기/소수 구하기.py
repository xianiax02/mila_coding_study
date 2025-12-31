start,end=map(int,input().split())


prime=list(range(2,end+1))

prime=[True]*(end-1)
for num in range(2,int(end**(1/2))+1): #끝을 제곱근으로 바꿔도 될거같은데
    if prime[num-2]:
        a=2
        while num*a<=end:
            prime[num*a-2]=False
            a+=1

for num in range(start,end+1):
    if num==1: #엣지케이스
        continue
    if prime[num-2]:
        print(num)