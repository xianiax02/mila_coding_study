import sys
n=int(sys.stdin.readline().strip())
scores=list(map(int,sys.stdin.readline().strip().split()))
maxnum=max(scores)
answer=sum(scores)*100/(maxnum*n)
print(answer)