def solution(array, commands):
    answer = []
    for (i,j,k) in commands:
        i-=1
        k-=1
        answer.append(sorted(array[i:j])[k])
    
    return answer