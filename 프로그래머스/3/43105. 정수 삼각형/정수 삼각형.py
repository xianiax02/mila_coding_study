def solution(triangle):
    height=len(triangle)
    d=[]
    for h in range(0,height):
        d.append([0]*(h+1))
    for h in range(0,height):
        for k in range(0,h+1):
            if k-1<0: #좌측 끝
                d[h][k]=d[h-1][k]+triangle[h][k]
            elif h-1<k: #우측 끝
                d[h][k]=d[h-1][k-1]+triangle[h][k]
            else:
                d[h][k]=max(d[h-1][k],d[h-1][k-1])+triangle[h][k]
            
    answer = max(d[height-1])
    return answer