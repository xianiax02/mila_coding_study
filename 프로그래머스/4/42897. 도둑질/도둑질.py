def solution(money):
    n=len(money)
    d1=[0]*(n)
    d2=[0]*(n-1)
    for i in range(n-1):
        d1[i]=d2[i]=money[i]
    d1[n-1]=money[n-1]
    for i in range(n-2,-1,-1):
        if i==n-2:
            d1[i]=max(money[i],d1[i+1])
        else:
            d1[i]=max(money[i]+d1[i+2],d1[i+1])
    for i in range(n-3,-1,-1):
        if i==n-3:
            d2[i]=max(money[i],d2[i+1])
        else:
            d2[i]=max(money[i]+d2[i+2],d2[i+1])
    if n>3:
        answer=max(money[0]+d2[2],d1[1])
    else:
        answer=max(money[0],d1[1])
    return answer