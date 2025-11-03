from collections import deque
import sys
input=sys.stdin.readline
n=int(input().strip())
queue=deque()
answer=[]
count=1
iteration=0
stop=False
while iteration<n and not stop:
    num=int(input().strip())
    if not queue or queue[-1]<num:
        for i in range(count,num+1):
            queue.append(i)
            answer.append('+')
        count=num+1
        queue.pop()
        answer.append('-')
    elif queue[-1]==num:
        queue.pop()
        answer.append('-')
    else:
        stop=True
    iteration+=1

if stop:
    sys.stdout.write('NO')
else:
    sys.stdout.write("\n".join(answer))
        
        