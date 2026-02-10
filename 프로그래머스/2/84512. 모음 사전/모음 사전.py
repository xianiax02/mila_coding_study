from itertools import product
from bisect import bisect_left
def solution(word):
    wordsset=set()
    for i in range(1,6):
        wordsset|=set([''.join(x) for x in product(['A','E','I','O','U'],repeat=i)])
    wordsset=list(wordsset)
    wordsset.sort()
    print(wordsset)
    idx=bisect_left(wordsset,word)
    answer=idx+1
    return answer