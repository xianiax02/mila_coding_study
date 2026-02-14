def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cctv=-float('inf')
    for route in routes:
        if route[0]<=cctv<=route[1]:
            continue
        else:
            cctv=route[1]
            answer+=1
    
    return answer