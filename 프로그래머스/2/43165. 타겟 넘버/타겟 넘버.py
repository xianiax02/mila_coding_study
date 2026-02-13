from collections import defaultdict
def solution(numbers, target):
    dp=dict()
    dp[0]=1
    for num in numbers:
        new_dp=dict()
        for n,cnt in dp.items():
            new_dp[n+num]=new_dp.get(n+num,0)+cnt
            new_dp[n-num]=new_dp.get(n-num,0)+cnt
        dp=new_dp
        print(dp)
    answer=dp.get(target,0)
    return answer