from itertools import permutations
def solution(numbers):
    
    answer = 0
    numbers=list(numbers)
    n=len(numbers)
    primenumbers=[True]*(int('9'*n)+1)
    primenumbers[0],primenumbers[1]=False,False
    maxnum=int(''.join(sorted(numbers,reverse=True)))
    for i in range(maxnum+1):
        if primenumbers[i]:
            k=2
            while i*k<maxnum+1:
                primenumbers[i*k]=False
                k+=1
    checked=set()
    for length in range(1,n+1):
        for numlist in permutations(numbers,length):
            num=int(''.join(numlist))
            if num in checked:
                continue
            else:
                checked.add(num)
            if primenumbers[num]:
                answer+=1
    return answer