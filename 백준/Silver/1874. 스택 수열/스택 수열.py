import sys
from collections import deque
n=int(sys.stdin.readline().strip())
datas=deque([])
count=1
prints=[]

NO=False
for i in range(n):
    num=int(sys.stdin.readline().strip())
    if count<=num: #count가 넘보다 작다==넘을 출력하려면 카운트를 증가시켜 계속 넣고 출력
        while count!=num+1:
            datas.append(count)
            prints.append('+')
            count+=1
        datas.pop()
        prints.append('-')
    else:
        if datas:
            if datas[-1]==num:
                datas.pop()
                prints.append('-')
            else:
                NO=True
                break
        else:
            NO=True
            break
            
if not NO:
    for i in prints:
        sys.stdout.write(i+'\n')
else:
    sys.stdout.write('NO')