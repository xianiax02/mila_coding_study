trinums=[]

for i in range(1,46):
	trinums.append((i**2+i)/2)
iterations=int(input())
givens=[]
for i in range(iterations):
	givens.append(int(input()))

for given in givens:
    answer=0
    for trinum1 in trinums:
        remain1=given-trinum1
        for trinum2 in trinums:
            remain2=remain1-trinum2
            if remain2 in trinums:
                answer=1
                break
        if answer==1:
            break
    print(answer)