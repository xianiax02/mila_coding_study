def createchessboard(n,color):
    chessboard=[]
    
    if color=='B':
        for _ in range(int(n/2)):
            row1=[]
            row2=[]
            for _ in range(int(n/2)):
                row1.append('B')
                row1.append('W')
            chessboard.append(row1)
            for _ in range(int(n/2)):
                row2.append('W')
                row2.append('B')
            chessboard.append(row2)
    if color=='W':
        for _ in range(int(n/2)):
            row1=[]
            row2=[]
            for _ in range(int(n/2)):
                row1.append('W')
                row1.append('B')
            chessboard.append(row1)
            for _ in range(int(n/2)):
                row2.append('B')
                row2.append('W')
            chessboard.append(row2)
    return chessboard

def checkchess(matrix,a,b):
    cnt1=0
    cnt2=0
    for i in range(8):
        for j in range(8):
            if (matrix[a+i][b+j]==chessboardB[i][j]):
                cnt1+=1
    for i in range(8):
        for j in range(8):
            if (matrix[a+i][b+j]==chessboardW[i][j]):
                cnt2+=1
    cnt=min(cnt1,cnt2)
    return cnt

chessboardW=createchessboard(8,'W')
chessboardB=createchessboard(8,'B')  
      
N,M=list(map(int,input().split(' ')))
matrix=[]
for _ in range(N):
   row=list(input())
   matrix.append(row)  



answer=9999999
for a in range(N-7):
    for b in range(M-7):
        answer=min(answer,checkchess(matrix,a,b))
        
print(answer)