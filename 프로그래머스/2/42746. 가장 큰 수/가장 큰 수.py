def solution(numbers):
    def extend(x,k):
        length=len(x)
        return x*(k//length)+x[:k%length]
    n=len(numbers)
    numbers=[str(x) for x in numbers]
    numbers.sort(key=lambda x: extend(x,4),reverse=True)
    answer=str(int(''.join(numbers)))
    return answer