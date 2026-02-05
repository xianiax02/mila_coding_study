def solution(routes):
    n=len(routes)
    visited=[False]*n
    cnt=0
    routes.sort(key=lambda x:x[1])
    for i, route in enumerate(routes):
        if not visited[i]:
            camera=route[-1]
            cnt+=1
            p=i
            while p<n and routes[p][0]<=camera<=routes[p][1]:
                visited[p]=True
                p+=1
    answer = cnt
    return answer