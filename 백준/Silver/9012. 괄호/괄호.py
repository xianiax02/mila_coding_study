import sys
from collections import deque

psdict={'(':')'}
def checkPS(string):
    a=deque([])
    for i in string:
        if i in psdict:
            a.append(i)
        else:
            if len(a)==0:
                print('NO')
                return
            else:
                val=a.pop()                
            if val in psdict:
                if i==psdict[val]:
                    continue
                else:
                    print('NO')
                    return
    if len(a)==0:
       print('YES')
       return
    else:
       print('NO')
       return

n=int(sys.stdin.readline().strip())
for _ in range(n):
    checkPS(sys.stdin.readline().strip())