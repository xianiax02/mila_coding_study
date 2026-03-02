string=input()
bomb=input()
stack=[]
for word in string:
    stack.append(word)
    if word==bomb[-1] and len(stack)>=len(bomb):
        if ''.join(stack[-len(bomb):])==bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
            