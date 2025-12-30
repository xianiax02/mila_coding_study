import sys
input=sys.stdin.readline
eq=input().strip().split('-')
numbers=[0]*len(eq)
for i in range(len(eq)):
    temp_sum = sum(map(int, eq[i].split('+')))
    numbers[i]=(temp_sum)

addition=numbers[0]
    
if len(numbers)!=1:
    
    subtraction=sum(numbers[1:])
    ans=addition-subtraction
else:
    ans=addition

print(ans)
    