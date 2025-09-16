def index2(matrix,num):
    for i in range(len(matrix)):
        if num in matrix[i]:
            return [i,matrix[i].index(num)]
        
        
def checkbingo(matrix):
    count=0
    for i in range(5):
        if sum(matrix[i])==0:
            count+=1
    for j in range(5):
        sum1=0
        for i in range(5):
            sum1+=matrix[i][j]
        if not sum1:
            count+=1
    sum2=0
    for i in range(5):
        sum2+=matrix[i][i]
    if not sum2:
        count+=1
    sum3=0
    for i in range(5):
        sum3+=matrix[4-i][i]
    if not sum3:
        count+=1
        
    if count>2:
        return 1
    else:
        return 0
    
    
matrix=[]
calledcount=0
foundbingo=0
for _ in range(5):
    row=list(map(int,input().split(' ')))
    matrix.append(row)
for i in range(5):
    called=list(map(int,input().split(' ')))
    for call in called:
        calledcount+=1
        index=index2(matrix,call)
        matrix[index[0]][index[1]]=0
        if checkbingo(matrix):
            foundbingo=1
            print(calledcount)
            break
    if foundbingo:
        break