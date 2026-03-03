#왼큰수 구하기
n=int(input())
towers=list(map(int,input().split()))
stack=[]
towers=[(num,i) for i,num in enumerate(towers)]
answer=[0]*n
for height,idx in towers[::-1]:
    while stack and stack[-1][0]<height:
        h,i=stack.pop()
        answer[i]=idx+1
    stack.append((height,idx))

print(*answer)
        