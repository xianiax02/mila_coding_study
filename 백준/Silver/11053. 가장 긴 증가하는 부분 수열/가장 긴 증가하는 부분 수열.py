from bisect import bisect_left
n=int(input())
numlist=list(map(int,input().split()))
dp=[]
for num in numlist:
    pos=bisect_left(dp,num)
    if pos>len(dp)-1:
        dp.append(num)
    else :
        dp[pos]=num

print(len(dp))
