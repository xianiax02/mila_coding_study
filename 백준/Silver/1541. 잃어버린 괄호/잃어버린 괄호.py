import sys
input=sys.stdin.readline
eq=input().strip()
numbers=[]
symbols=['+'] #처음 숫자는 무조건 양수
startindex=0
for i in range(len(eq)):
    if eq[i]=='+' or eq[i]=='-' :
        #if i == startindex:
         #   numbers.append()
        numbers.append(int(eq[startindex:i]))
        symbols.append(eq[i])
        startindex=i+1
    elif i==len(eq)-1:
        numbers.append(int(eq[startindex:]))
        symbols.append(eq[i])
ans=sum(numbers)
if '-' in symbols:
    firstsub=symbols.index('-')
    addition=sum(numbers[:firstsub])
    subtraction=sum(numbers[firstsub:])
    ans=addition-subtraction
    

print(ans)

        