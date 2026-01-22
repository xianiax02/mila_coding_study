def solution(n,a,b):
    cnt = 0
    #num-1=index
    a-=1
    b-=1
    while a!=b:
        a=a//2
        b=b//2
        cnt+=1

    return cnt