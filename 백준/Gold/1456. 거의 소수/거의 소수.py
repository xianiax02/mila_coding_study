start,end=map(int,input().split())
halfend=int(end**(1/2))+1
numbers=[1]*(halfend+1) #인덱스 통일을 위해 0패딩(나중가서는 0이 아닌 곳 출력하니 상관 x) 처음 소수 배열 구할때 제곱근 까지만 거의 소수를 구성할 소수가 존재하니
#결국은 거의 소수를 찾는 거기 때문에 모든 소수를 찾을 필요는 없다!
numbers[0]=0
numbers[1]=0
primes=[]
#소수 남기기 
for num in range(2,halfend):
    if numbers[num]:
        for mul in range(num+num,halfend+1,num): #어차피 자기보다 작은 숫자는 곱해도 이미 그 작은 숫자차례에서 지워짐.
            numbers[mul]=0
        primes.append(num)

#초기화하고 거의 소수 찾기 에라토스테네스 체 방식으로 구하기엔 배열 크기가 너무 큼. 조건문을 붙여서, 숫자비교 조건만으로 카운트
cnt=0
for prime in primes:
    almostprime=prime**2
    while almostprime<=end:
        if start<=almostprime:
            cnt+=1
        almostprime*=prime
        
print(cnt)  

    