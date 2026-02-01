def solution(numbers, target):
    n=len(numbers)
    dp=[0]*(1<<n) #n+1자리수가 됨.
    for i in range(n):
        num=numbers[i]
        temp=dp[:]
        for index in range(1<<i):
            value=temp[index]
            leftindex=(index<<1)
            rightindex=(index<<1)+1
            dp[leftindex]=value-num
            dp[rightindex]=value+num
    answer = dp.count(target)
    return answer