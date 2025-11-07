from queue import PriorityQueue
import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
pq=PriorityQueue()

for _ in range(n):
    num=int(input().strip())
    if num==0:
        if not pq.empty():
            print(str(pq.get()[1])+'\n')
        else:
            print('0\n')
    else:
        pq.put((abs(num),num))