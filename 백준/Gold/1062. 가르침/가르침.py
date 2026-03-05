import sys
from itertools import combinations
input=sys.stdin.readline
n,k=map(int,input().split())
basics=0
for ch in 'antic':
    ch=ord(ch)-ord('a')
    basics|=1<<ch
    
words=[]
for _ in range(n):
    wordtonum=0
    word=input().strip()
    for char in word:
        char=ord(char)-ord('a') #a--> 1
        wordtonum|=1<<char
    words.append(wordtonum)

if k<5:
    print(0)

else:
    answer=0
    candnumbers=[1<<i for i in range(26) if not (basics&(1<<i))]
    candidates=combinations(candnumbers,k-5)
    for candidate in candidates:
        inthiscase=0
        learned=basics|sum(candidate)
        for word in words:
            if (learned&word)==word :
                inthiscase+=1
        answer=max(answer,inthiscase)
    print(answer)