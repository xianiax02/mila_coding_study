import sys
n=int(sys.stdin.readline())
numbers=[int(sys.stdin.readline().strip()) for _ in range(n)]
numbers.sort()
for number in numbers:
    sys.stdout.write(str(number)+'\n')