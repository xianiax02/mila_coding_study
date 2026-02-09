def solution(sizes):
    sizes=[sorted(x) for x in sizes]
    a=max([x[0] for x in sizes])
    b=max([x[1] for x in sizes])
    answer = a*b
    return answer