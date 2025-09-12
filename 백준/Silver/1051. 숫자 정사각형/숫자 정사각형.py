N,M=list(map(int,(input().split(' '))))
mat=[]
for _ in range(N):
	row=[]
	num=input()
	for i in range(M):
		row.append(int(num[i]))
	mat.append(row)

answer=0
for i in range(N):
	for j in range(M):
		base=mat[i][j]
		for k in range(M-1,j-1,-1): #M끝에서 부터 시작
			
			if (mat[i][k]==base):
				side=k-j+1 #변의 길이
				if (i+side-1)<N : #아래로 범위를 벗어나는지 확인
				    if(mat[i+side-1][j]==base)&(mat[i+side-1][k]==base):        
					    answer=max(side**2,answer)
					    break #해당 줄에서 가장 큰 정사각형은 찾음

print(answer)		
				