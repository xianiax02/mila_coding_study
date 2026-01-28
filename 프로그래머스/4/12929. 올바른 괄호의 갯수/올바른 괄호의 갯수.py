def solution(n):
    d=[0]*(n+1)
    d[0]=1
    for k in range(n+1):
        for i in range(n):
            d[k]+=d[i]*d[k-1-i]
    answer = d[n]
    return answer